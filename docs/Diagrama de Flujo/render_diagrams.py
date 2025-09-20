import os, subprocess, shutil, glob

def ensure_graphviz():
    try:
        subprocess.run(["dot","-V"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception:
        return False

def render_all(input_dir=".", out_dir="./png"):
    os.makedirs(out_dir, exist_ok=True)
    for dot_path in glob.glob(os.path.join(input_dir, "*.dot")):
        name=os.path.splitext(os.path.basename(dot_path))[0]
        png_path=os.path.join(out_dir, name + ".png")
        cmd=["dot","-Tpng",dot_path,"-o",png_path]
        subprocess.run(cmd, check=True)
        print("OK ->", png_path)

if __name__ == "__main__":
    if not ensure_graphviz():
        print("Graphviz no está instalado. En Colab: !apt-get -y install graphviz")
    else:
        render_all(input_dir=".", out_dir="./png")
