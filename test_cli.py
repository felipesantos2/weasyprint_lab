import uuid
import sys
import os
from pathlib import Path

import pytest
from jinja2 import Template
from rich.console import Console

from cli import (
    load_html_template,
    render_jinja_template,
    settings,
    write_html_file,
    write_pdf_file,
)

console = Console()

PDF_DOC_OUTPUT = uuid.uuid4()

HTML_BASE_TEMPLATE = Path("./templates/template.jinja2.html")


# verifica se há um retorno de um html
def test_jinja_html_template_loaded():
	""" testa se o arquivo de template base é carregado """
	template_str_content = load_html_template(HTML_BASE_TEMPLATE)

	assert "DOCTYPE" in template_str_content
	assert "html" in template_str_content


def test_jinja_html_template_generated():
	""" testa se arquivo de template em html é gerado """
	template_str_content = load_html_template(HTML_BASE_TEMPLATE)

	merge_context_data: dict = settings
	html_out_content = render_jinja_template(Template(template_str_content), merge_context_data)

	output_file = Path("./templates/template_debug.html")
	html_file = write_html_file(html_out_content, output_file)

	assert True == html_file.exists()
	assert True == html_file.is_file()
	assert Path("./templates/template_debug.html") ==  html_file


def test_pdf_document_is_generated():
	""" testa se arquivo em pdf é gerado """
	template_str_content = load_html_template(HTML_BASE_TEMPLATE)

	merge_context_data: dict = settings
	html_out_content = render_jinja_template(Template(template_str_content), merge_context_data)

	output_file = Path("./templates/template_debug.html")
	html_file = write_html_file(html_out_content, output_file)

	output_file = Path(f"./templates/reports/pdf/{PDF_DOC_OUTPUT}.pdf")
	pdf_file = write_pdf_file(html_out_content, output_file)

	assert "DOCTYPE" in template_str_content
	assert "html" in template_str_content

	assert True == html_file.exists()
	assert True == html_file.is_file()
	assert Path("./templates/template_debug.html") ==  html_file

	assert True == pdf_file.exists()
	assert True == pdf_file.is_file()
	assert output_file == pdf_file
