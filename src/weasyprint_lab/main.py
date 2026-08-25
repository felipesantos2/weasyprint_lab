from rich.console import Console
from weasyprint_lab import cli

console = Console()

def app() -> None:
    cli.run()

if __name__ == '__main__':
    app()
