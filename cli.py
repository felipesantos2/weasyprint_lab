"""
Start Dev web server:
    flask run --reload
    uv run flask run --reload

Run in terminal:
    uv run app.py
    ruff format app.py
    ruff check app.py
"""
from docutils.parsers.rst.directives import encoding
from importlib.resources import path

import datetime
import os
from pathlib import Path
from zoneinfo import ZoneInfo

from jinja2 import Template
from rich.console import Console
from weasyprint import HTML

date_time = datetime.datetime

console = Console()

HTML_BASE_TEMPLATE = "template.jinja2.html"

settings: dict[str, str] = {
    "title": "Relatório Base",
    "author": "@felipesantos2",
    "created_at ": str(date_time.now(tz=ZoneInfo("America/Sao_Paulo"))),
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



def run() -> None:
    try:
        template_path = f"./templates/{HTML_BASE_TEMPLATE}"
        template_path = os.path.abspath(template_path)
        template_str = load_html_template(template_path)

        merge_context_data: dict = settings
        html_out = render_jinja_template(Template(template_str), merge_context_data)

        # write_html_file(html_out)

        tmp_pdf = write_pdf_file(html_out)
    except Exception as e:  # noqa: BLE001
        console.log(f"Erro! Exception: {e} ")
    else:
        console.log("tmp file: ", tmp_pdf)
        console.log("PDF Gerado com Sucesso! ")


if __name__ == "__main__":
    run()
