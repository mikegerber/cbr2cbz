import os
import subprocess
import tempfile
import zipfile

from loguru import logger

UNRAR = "unrar-free"


def unpack_cbr(cbr_path, output_folder):
    """Unpack a .cbr file using unrar."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    command = [UNRAR, "x", "-o+", cbr_path, output_folder]
    result = subprocess.run(command, check=False, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Unrar failed:\n{result.stderr}")
    else:
        logger.debug(f"Unpacked '{cbr_path}' to '{output_folder}'")


def pack_cbz(input_folder, cbz_path):
    """Repack folder content into a .cbz file (zip)."""
    if os.path.exists(cbz_path):
        raise RuntimeError(f"'{cbz_path}' already exists")
    tmp_cbz_path = cbz_path.with_suffix(".cbz-tmp")
    with zipfile.ZipFile(tmp_cbz_path, "w", zipfile.ZIP_DEFLATED) as cbz:
        for root, _, files in os.walk(input_folder):
            for file in sorted(files):
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_folder)
                cbz.write(file_path, arcname)
    os.rename(tmp_cbz_path, cbz_path)
    logger.info(f"Packed '{cbz_path}'")


def convert_cbr_to_cbz(cbr_path, cbz_path):
    with tempfile.TemporaryDirectory() as temp_dir:
        unpack_cbr(cbr_path, temp_dir)
        pack_cbz(temp_dir, cbz_path)
