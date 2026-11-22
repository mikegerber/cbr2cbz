from pathlib import Path

import click
from loguru import logger

from .cbr2cbz import convert_cbr_to_cbz


@click.command()
@click.argument("cbrs", nargs=-1, type=click.Path())
@click.option("-v", "--verbose", is_flag=True, help="Be verbose.")
def convert(cbrs, verbose):
    logger.remove()
    if verbose:
        level = "DEBUG"
    else:
        level = "INFO"
    logger.add(
        sink=lambda msg: click.echo(msg, nl=False),
        level=level,
        colorize=True,
        format="<green>{time:HH:mm:ss}</green> | <level>{level:<7}</level> | {message}",
    )

    for cbr in cbrs:
        cbr = Path(cbr)
        if cbr.suffix != ".cbr":
            raise RuntimeError(f"{cbr} does not end with .cbr")
        cbz = cbr.with_suffix(".cbz")
        convert_cbr_to_cbz(cbr, cbz)


if __name__ == "__main__":
    convert()
