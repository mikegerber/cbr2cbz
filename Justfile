default:
  @just --list

test:
  rm -f example example.cbz
  uv run cbr2cbz example.cbr
