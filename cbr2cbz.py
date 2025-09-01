import os
import shutil
import zipfile
import tempfile
import subprocess
import click
from pathlib import Path

from loguru import logger


UNRAR = "unrar-free"


def unpack_cbr(cbr_path, output_folder):
    """Unpack a .cbr file using unrar."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    command = [UNRAR, "x", "-o+", cbr_path, output_folder]
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    if result.returncode != 0:
        raise RuntimeError(f"Unrar failed:\n{result.stderr}")
    else:
        logger.debug(f"Unpacked '{cbr_path}' to '{output_folder}'")


def pack_cbz(input_folder, cbz_path):
    """Repack folder content into a .cbz file (zip)."""
    if os.path.exists(cbz_path):
        raise RuntimeError(f"'{cbz_path}' already exists")
    with zipfile.ZipFile(cbz_path, "w", zipfile.ZIP_DEFLATED) as cbz:
        for root, _, files in os.walk(input_folder):
            for file in sorted(files):
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_folder)
                cbz.write(file_path, arcname)
    logger.info(f"Packed '{cbz_path}'")


def convert_cbr_to_cbz(cbr_path, cbz_path):
    with tempfile.TemporaryDirectory() as temp_dir:
        unpack_cbr(cbr_path, temp_dir)
        pack_cbz(temp_dir, cbz_path)


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
