# cbr2cbz

Convert comic books in the CBR format to the CBZ format. CBR comic books are just image files in
a RAR archive. This tool repacks these into a ZIP file (CBZ), which is supported by more reader
apps.


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
