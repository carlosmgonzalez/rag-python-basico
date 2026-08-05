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
                    pages_text.append(f"[Pagina {page_number}\n{page_text}")

            return "\n\n".join(pages_text)

        except (OSError, PdfReadError) as error:
            console.print(f"[red]Error leyendo {pdf_path.name}: {error}[/red]")
            return None

    @staticmethod
    def list_pdfs(folder: Path) -> list[Path]:
        if not folder.exists():
            folder.mkdir(parents=True, exist_ok=True)

        return list(folder.glob("*.pdf"))
