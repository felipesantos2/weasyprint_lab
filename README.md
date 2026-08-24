# weasyprint_lab

Uma breve demonstração da **renderização** de PDFs usando Python, Jinja2 e **WeasyPrint**

O projeto explora um fluxo simples para gerar modelos HTML com o Jinja2 e convertê-los em documentos PDF usando o WeasyPrint.

---

### STACK
- Python
- UV
- Jinja2
- WeasyPrint
- Flask
- Rich CLI
### SETUP
`sync dependecies:`
```bash
    uv sync
```
`run script:`
```bash
    uv run app.py
```
`run tests:`
```bash
    uv run pytest
```
```bash
    pytest
```
### NOTAS

Os testes estão evoluindo gradualmente. Primeiro escrevi funções básicas para carregar e criar os arquivos. Agora adicionei uma função para deletar esses arquivos gerados, evitando o acumulo desnecessário.
---
**Conceito Importante:** 

Esses tipos de testes devem evitar operações com **I/O** ou de alguma forma mascarar esse comportamento, pois em um cenário hipotético onde podemos temos centena de testes, aqui é onde surgiria um grande gargalo. Testes unitários precisão ser rápidos para fazer sentido existirem.
