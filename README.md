# cbr2cbz

Convert comic books from CBR to CBZ format. CBR files are essentially RAR archives containing
images. This tool repackages them as ZIP archives (CBZ), which are supported by more comic book
readers.


## Requirements

- unrar-free
- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/) (recommended for installation)


## Installation

Install the command directly from the Git repository:

```sh
uv tool install "git+https://cvs.moegen-wir.net/mikegerber/cbr2cbz.git"
```

Alternatively, run it from a checkout:

```sh
git clone https://cvs.moegen-wir.net/mikegerber/cbr2cbz.git
uv run --project /path/to/cbr2cbz cbr2cbz
```


## Usage

Run the command from the command line:

```sh
cbr2cbz example.cbr
```
