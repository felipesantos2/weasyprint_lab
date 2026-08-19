import sys
import os
from pathlib import Path

import pytest
from jinja2 import Template
from rich.console import Console

from cli import (
    HTML_BASE_TEMPLATE,
    load_html_template,
    render_jinja_template,
    settings,
    write_html_file,
    write_pdf_file,
)

console = Console()


# verifica se há um retorno de um html
def test_load_html_jinja_template():
    template_path = os.path.abspath(f"./templates/{HTML_BASE_TEMPLATE}")
    template_str_content = load_html_template(template_path)
    first_word = (
        template_str_content.split("\n")[0].split(" ")[0].split("!")[1]
    )  # get DOCKTYPE
    assert "DOCTYPE" == first_word


def test_html_template_file_generated():
    template_path = os.path.abspath(f"./templates/{HTML_BASE_TEMPLATE}")
    template_str = load_html_template(template_path)

    merge_context_data: dict = settings
    template_objct = Template(template_str)

    html_out = render_jinja_template(template_objct, merge_context_data)
    html_file = write_html_file(html_out)
    assert Path(html_file).is_file()


def test_pdf_document_is_generated():
    template_path = Path("./templates/template.jinja2.html")
    template_str = load_html_template(template_path)

    html_out = render_jinja_template(Template(template_str), settings)

    assert write_pdf_file(html_out) == template_path
