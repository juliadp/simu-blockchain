#!/usr/bin/env python3
# docs/diagrams/render_diagrams.py
import os, sys, glob, subprocess

INPUT_DIR = "docs/diagrams"
OUT_DIR   = "docs/diagrams/build"

def ensure_graphviz() -> bool:
    try:
        subprocess.run(["dot", "-V"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except Exception:
        return False

def render_one(dot_path: str) -> None:
    base = os.path.splitext(os.path.basename(dot_path))[0]
    out_path = os.path.join(OUT_DIR, f"{base}.png")
    os.makedirs(OUT_DIR, exist_ok=True)

    # Cache: saltear si el PNG está más nuevo que el .dot
    if os.path.exists(out_path) and os.path.getmtime(out_path) >= os.path.getmtime(dot_path):
        print(f"skip (up-to-date) -> {out_path}")
        return

    subprocess.run(["dot", "-Tpng", dot_path, "-o", out_path], check=True)
    print(f"OK   -> {out_path}")

def main():
    if not ensure_graphviz():
        print(
            "Graphviz no está instalado.\n"
            "Windows:  winget install Graphviz.Graphviz\n"
            "Ubuntu:   sudo apt-get update && sudo apt-get -y install graphviz"
        )
        sys.exit(1)

    paths = sorted(glob.glob(os.path.join(INPUT_DIR, "*.dot")))
    if not paths:
        print(f"Sin .dot en {INPUT_DIR}")
        return

    for p in paths:
        try:
            render_one(p)
        except subprocess.CalledProcessError as e:
            print(f"ERR  -> {p}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()