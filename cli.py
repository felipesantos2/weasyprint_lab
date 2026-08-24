import datetime as dt
import os
import sys
import uuid
from pathlib import Path
from zoneinfo import ZoneInfo

from jinja2 import Template
from rich.console import Console
from weasyprint import HTML

console = Console()

PDF_DOC_OUTPUT = uuid.uuid4()
HTML_BASE_TEMPLATE = Path("./templates/template.jinja2.html")

settings: dict[str, str] = {
    "title": "Relatório Base",
    "author": "@felipesantos2",
    "created_at": str(
        dt.datetime.now(tz=ZoneInfo("America/Sao_Paulo")).strftime("%d-%m-%Y")
    ),
}


def load_html_template(file: Path) -> str:
    console.log("template base: ", file)
    return file.read_text(encoding="utf-8")


def render_jinja_template(template: Template, data: dict) -> str:
    return template.render(**data)


def write_html_file(html_out_content: str, file: Path) -> Path:
    with open(file, "w", encoding="utf-8") as f:
        f.write(html_out_content)
    return file


def write_pdf_file(html_out: str, file: Path) -> Path:
    Path("./templates/reports/pdf").mkdir(parents=True, exist_ok=True)
    HTML(string=html_out).write_pdf(file)
    return file


def delete_file(file: Path) -> bool:
    if file.is_file():
        os.remove(file)
        console.log(f"file: [{file}] deletado com sucesso!")
        return True
    return False


def run() -> int:
    try:
        # 0 -> OK 1 - Fail
        template_str_content = load_html_template(HTML_BASE_TEMPLATE)

        merge_context_data: dict = settings
        html_out_content = render_jinja_template(
            Template(template_str_content), merge_context_data
        )

        output_file = Path("./templates/template_debug.html")
        html_file = write_html_file(html_out_content, output_file)  # noqa

        output_file = Path(f"./templates/reports/pdf/{PDF_DOC_OUTPUT}.pdf")
        pdf_file = write_pdf_file(html_out_content, output_file)

        # Aqui podemos adicionar lógicas de upload em um bucket GCS, S3, Drive e até mesmo deixar no disco
        delete_file(output_file)

        console.log("tmp file: ", pdf_file)
        console.log("PDF Gerado e deletado com Sucesso! ")

        raise SystemExit(0)
    except Exception as e:  # noqa: BLE001
        console.log(f"Erro! Exception: {e} ")
        raise SystemExit(1)


if __name__ == "__main__":
    run()
