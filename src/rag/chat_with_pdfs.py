from ast import While
from pathlib import Path

from dotenv import load_dotenv
from pypdf import PdfReader
from pypdf.errors import PdfReadError
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from src.rag.rag_pipeline import RAGPipeline

load_dotenv()
console = Console()


class PDFProcessor:
    @staticmethod
    def extract_text(pdf_path: Path) -> str:
        try:
            reader = PdfReader(stream=str(pdf_path))
            pages_text = []

            for page_number, page in enumerate(reader.pages, 1):
                page_text = page.extract_text()

                if page_text and page_text.strip():
                    pages_text.append(f"[Pagina {page_number}]\n{page_text}")

            return "\n\n".join(pages_text)

        except (OSError, PdfReadError) as error:
            console.print(f"[red]Error leyendo {pdf_path.name}: {error}[/red]")
            return ""

    @staticmethod
    def list_pdfs(folder: Path) -> list[Path]:
        if not folder.exists():
            folder.mkdir(parents=True, exist_ok=True)

        return list(folder.glob("*.pdf"))


class IndexRegistry:
    def __init__(self, registry_path: Path):
        self.path = registry_path
        self.registry: dict[str, int] = {}
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return

        with open(self.path, "r") as file:
            for line in file.read().splitlines():
                if not line.strip():
                    continue

                parts = line.rsplit(":", 1)

                if len(parts) == 2:
                    name, size = parts
                    self.registry[name] = int(size)

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.path, "w") as file:
            for name, size in self.registry.items():
                file.writelines(f"{name}:{size}")

    def is_indexed(self, pdf_path: Path) -> bool:
        if pdf_path.name not in self.registry:
            return False

        current_size = pdf_path.stat().st_size
        return self.registry[pdf_path.name] == current_size

    def mark_indexed(self, pdf_path: Path) -> None:
        self.registry[pdf_path.name] = pdf_path.stat().st_size

    @property
    def indexed_names(self) -> list[str]:
        return sorted(self.registry.keys())

    @property
    def count(self) -> int:
        return len(self.registry)


class ChatWithPDFs:
    def __init__(self, pdf_folder: str = "./data/pdfs"):
        self.pdf_folder = Path(pdf_folder)
        self.processor = PDFProcessor()
        self.registry = IndexRegistry(registry_path=Path("./data/pdfs_indexed.txt"))

        self.rag = RAGPipeline(
            collection_name="knowledge_base", db_path="./data/chromadb_pdfs"
        )

    def index_new_pdfs(self) -> int:

        pdfs = self.processor.list_pdfs(self.pdf_folder)
        if not pdfs:
            console.print(f"[yellow]No hay PDFs en {self.pdf_folder}[/yellow]\n")
            return 0

        news_pdfs = [pdf for pdf in pdfs if not self.registry.is_indexed(pdf)]

        if not news_pdfs:
            console.print("[green]Todos los PDFs estan indexados[/green]")
            return 0

        console.print("[bold cyan]Indexando...[/bold cyan]")

        indexed_count = 0

        for pdf_path in news_pdfs:
            pdf_text = self.processor.extract_text(pdf_path=pdf_path)
            if not pdf_text.strip():
                console.print("[red]Sin texto extraible[/red]")
                continue

            num_chunks = self.rag.index_chunks(
                long_text=pdf_text, base_metadata={"fuente": pdf_path.name}
            )

            console.print(
                f"[green]PDF {pdf_path.name} indexado correcctamente, numero de chunks: {num_chunks}[/green]"
            )
            self.registry.mark_indexed(pdf_path)

            indexed_count += 1

        self.registry.save()
        return indexed_count

    def show_status(self) -> None:
        table = Table(title="Estado del Sistema RAG", show_header=True)
        table.add_column("Métrica", style="cyan")
        table.add_column("Valor", style="green")

        table.add_row("PDFs indexados", str(self.registry.count))
        table.add_row("Fragmentos en ChromaDB", str(self.rag.collection.count()))
        table.add_row("Carpeta de PDFs", str(self.pdf_folder))
        table.add_row("Modelo embeddings", "text-embedding-3-small")
        table.add_row("Modelo respuesta", "gpt-5.6-luna")

        console.print(table)

        if self.registry.indexed_names:
            console.print("\n[bold]PDFs en la base de conocimiento:[/bold]")
            for name in self.registry.indexed_names:
                console.print(f"  📄 {name}")

    def chat(self) -> None:
        console.print(
            Panel.fit(
                "[bold cyan]Chat con tus PDFs[/bold cyan]\n"
                "[dim]Comandos disponibles: 'estado' | 'reindexar' | 'salir'[/dim]",
                border_style="cyan",
            )
        )

        if self.rag.collection.count() == 0:
            console.print(
                "\n[yellow]⚠️  La base de conocimiento está vacía.[/yellow]\n"
                f"Coloca PDFs en [bold]{self.pdf_folder}[/bold] "
                "y escribe 'reindexar'\n"
            )

        while True:
            try:
                question = console.input("[bold green]Tu:[/bold green]").strip()

                if not question:
                    continue

                if question.lower() in ("salir", "exit"):
                    console.print("\n[dim]Hasta luego[/dim]\n")
                    break

                if question.lower() == "estado":
                    self.show_status()
                    continue

                if question.lower() == "reindexar":
                    self.index_new_pdfs()
                    continue

                with console.status("[dim]Buscando en tus documentos...[/dim]"):
                    result = self.rag.answer(question=question)
                    console.print(
                        Panel(
                            result["response"], title="Asistente", border_style="blue"
                        )
                    )

            except Exception as e:
                pass


if __name__ == "__main__":
    pdf_path = Path("./proton-recovery-phrase.pdf")
    # registry = IndexRegistry(pdf_path)

    pdf_text = PDFProcessor.extract_text(pdf_path)
    print(pdf_text)
