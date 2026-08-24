# weasyprint_lab

A brief demonstration of PDF **rendering** using Python, Jinja2, and **WeasyPrint**

The project explores a simple workflow for generating HTML templates with Jinja2 and converting them into PDF documents using WeasyPrint.

---

### STACK
- Python
- UV
- Jinja2
- WeasyPrint
- Flask
- Rich CLI
### SETUP
sync dependecies:
```bash
    uv sync
```
run script
```bash
    uv run app.py
```
### NOTAS
Os testes estão evoluindo gradualemente. Primeto escrevi funções básicas para carregar e criar os arquivos. Agora adicionei uma função para deletar esses documentos gerados, evitanto o acumulo desnecessário.

**Conceito Inportante:** Esses tipos de teste devem evitar operações com **I/O** ou de alguma forma mascarar esse comportamento, pois em um cenário hipotético onde podemos temos centena de testes, aqui surgiria um grande garga-lo. Testes unitários precisão ser rápidos para fazer sentido existirem.