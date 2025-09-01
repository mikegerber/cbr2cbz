{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    (pkgs.python3.withPackages (ps: [
      ps.loguru
      ps.click

      ps.black
    ]))
    pkgs.unrar-free
  ];
}
