import sys
from pathlib import Path

from dotenv import load_dotenv
from pypdf import PdfReader
from pypdf.errors import PdfReadError
from rich.console import Console

from src.rag.rag_pipeline import RAGPipeline

load_dotenv()
console = Console()


class PDFProcessor:
    @staticmethod
    def extract_text(pdf_path: Path) -> str | None:
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
            return None

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

        return True


if __name__ == "__main__":
    pdf_path = Path(
        "/Users/carlos/Code/curso-python-ia/rag-python-basico/proton-recovery-phrase.pdf"
    )
    # registry = IndexRegistry(pdf_path)

    pdf_text = PDFProcessor.extract_text(pdf_path)
    print(pdf_text)
