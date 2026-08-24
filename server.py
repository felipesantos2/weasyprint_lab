"""
Start Dev web server:
    flask run --reload
    uv run flask run --reload

Run in terminal:
    uv run app.py
    ruff format app.py
    ruff check app.py
"""

import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from flask import Flask
from jinja2 import Template
from rich.console import Console
from weasyprint import HTML

console = Console()

HTML_BASE_TEMPLATE = "template.jinja2.html"

settings: dict[str, str] = {
    "title": "Relatório Base",
    "author": "@felipesantos2",
    "created_at ": str(datetime.now(tz=ZoneInfo("America/Sao_Paulo"))),
}


def load_html_template(file_path: str) -> str:
    console.log("template base: ", file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        template_str = f.read()
    return template_str


def render_jinja_template(template: Template, data: dict) -> str:
    return template.render(**data)


def write_html_file(html_out: str) -> None:
    file = os.path.abspath("./templates/template_debug.html")
    with open(file, "w", encoding="utf-8") as f:
        f.write(html_out)


def write_pdf_file(html_out: str) -> str:
    import uuid

    uuid4 = uuid.uuid4()

    Path("./templates/reports/pdf").mkdir(parents=True, exist_ok=True)
    output_path = f"./templates/reports/pdf/{uuid4}.pdf"

    output_pdf = os.path.abspath(output_path)
    HTML(string=html_out).write_pdf(output_pdf)
    return output_pdf


def run() -> None:
    try:
        template_path = f"./templates/{HTML_BASE_TEMPLATE}"
        template_path = os.path.abspath(template_path)
        template_str = load_html_template(template_path)

        merge_context_data: dict = settings

        template_objct = Template(template_str)
        html_out = render_jinja_template(template_objct, merge_context_data)

        write_html_file(html_out)

        tmp_pdf = write_pdf_file(html_out)
    except Exception as e:  # noqa: BLE001
        console.log(f"Erro! Exception: {e} ")
    else:
        console.log("tmp file: ", tmp_pdf)
        console.log("PDF Gerado com Sucesso! ")


app = Flask(__name__)


@app.route("/")
def home():
    run()
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
