import typer
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

app = typer.Typer()


@app.command()
def main(path: str):
    typer.echo(f"Fixing {path}")
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    [pdf_writer.addPage(page) for page in properly_format(pdf.pages)]

    with Path(f"fixed-{path}.pdf").open(mode="wb") as output_file:
        pdf_writer.write(output_file)


def properly_format(pages):
    duplicated_pages = list(pages)
    result = []
    while len(duplicated_pages) > 0:
        first = duplicated_pages.pop(0)
        last = duplicated_pages.pop()
        result.append(first)
        result.append(last)
    return result
