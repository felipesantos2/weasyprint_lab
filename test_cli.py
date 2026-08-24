import os
import sys
import tempfile as tp
import uuid
from pathlib import Path

from jinja2 import Template
from rich.console import Console

from cli import (
    delete_file,
    load_html_template,
    render_jinja_template,
    run,
    settings,
    write_html_file,
    write_pdf_file,
)

console = Console()

PDF_DOC_OUTPUT = uuid.uuid4()
HTML_BASE_TEMPLATE = Path("./templates/template.jinja2.html")


def test_jinja_html_template_loaded():
    """testa se o arquivo de template base é carregado"""
    template_str_content = load_html_template(HTML_BASE_TEMPLATE)

    assert "DOCTYPE" in template_str_content
    assert "html" in template_str_content


def test_jinja_html_template_generated():
    """testa se arquivo de template em html é gerado"""
    template_str_content = load_html_template(HTML_BASE_TEMPLATE)

    merge_context_data: dict = settings
    html_out_content = render_jinja_template(
        Template(template_str_content), merge_context_data
    )

    output_file = Path("./templates/template_debug.html")
    html_file = write_html_file(html_out_content, output_file)

    assert html_file.exists()
    assert html_file.is_file()
    assert Path("./templates/template_debug.html") == html_file


def test_delete_file_successfuly():
    with tp.NamedTemporaryFile(suffix=".pdf") as t:
        tmp_file = t.name

    # console.log(Path(tmp_file).parent)

    path = Path(tmp_file)

    assert "/tmp" == str(path.parent)
    assert Path(tmp_file).is_file()
    ## WARNING - break
    assert delete_file(path)


def test_delete_file_failed():
    deleted = delete_file(
        Path("./templates/reports/pdf/74a4c7fe-e30e-49a5-94db-cf368d760748.pdf")
    )
    assert False == deleted


def test_run():
    """testa o método inicial [run] é execurado com sucesso"""
    value: int = run()
    assert 0 == value


def test_pdf_document_is_generated():
    """testa se o documento em pdf é gerado"""
    template_str_content = load_html_template(HTML_BASE_TEMPLATE)

    merge_context_data: dict = settings
    html_out_content = render_jinja_template(
        Template(template_str_content), merge_context_data
    )

    output_file = Path("./templates/template_debug.html")
    html_file = write_html_file(html_out_content, output_file)

    output_file = Path(f"./templates/reports/pdf/{PDF_DOC_OUTPUT}.pdf")
    pdf_file = write_pdf_file(html_out_content, output_file)

    assert "DOCTYPE" in template_str_content
    assert "html" in template_str_content

    assert html_file.exists()
    assert html_file.is_file()
    assert Path("./templates/template_debug.html") == html_file

    assert pdf_file.exists()
    assert pdf_file.is_file()
    assert output_file == pdf_file

    deleted = delete_file(output_file)

    assert True == deleted
