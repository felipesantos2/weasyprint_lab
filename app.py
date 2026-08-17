"""
Executa o servidor para desenvolvimento
    flask run --reload
    uv run flask run --reload
    uv run app.py
"""

from flask import Flask
from rich.console import Console
from jinja2 import Environment, PackageLoader, select_autoescape, Template
import tempfile
from weasyprint import HTML
from datetime import datetime
from zoneinfo import ZoneInfo
import os
from pathlib import Path


RELATORIO_FINAL = "relatorio_anual_final.pdf"
HTML_BASE_TEMPLATE = "template.jinja2.html"

headers: dict[str, str] = {
    "title": "Relatório Base",
    "created_at ": str(datetime.now(tz=ZoneInfo("America/Sao_Paulo"))),
}
info: dict[str, str] = {"author": "@felipesantos2"}

console = Console()


def load_html_template(file_path: str) -> str:
    print("template base: ", file_path)

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
    Path("./templates/reports/pdf").mkdir(parents=True, exist_ok=True)
    output_path = f"./templates/reports/pdf/{RELATORIO_FINAL}"

    output_pdf = os.path.abspath(output_path)
    HTML(string=html_out).write_pdf(output_pdf)
    return output_pdf


def main() -> None:
    try:
        template_path = f"./templates/{HTML_BASE_TEMPLATE}"
        template_path = os.path.abspath(template_path)
        template_str = load_html_template(template_path)

        merge_context_data = headers | info

        template_objct = Template(template_str)
        html_out = render_jinja_template(template_objct, merge_context_data)

        write_html_file(html_out)

        tmp_pdf = write_pdf_file(html_out)
    except Exception as e:
        print(f"Erro! Exception: {e} ")
    else:
        print("tmp file: ", tmp_pdf)
        print("PDF Gerado com Sucesso! ")


# app = Flask(__name__)


# @app.route("/")
# def home():
#     return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    main()
    # app.run(host="127.0.0.1", port=8000, debug=True)
