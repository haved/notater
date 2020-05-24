#!/usr/bin/env python3

from sys import argv
from subprocess import Popen
from os.path import join, isdir
from os import rename, mkdir
from shutil import copytree, rmtree

PAGE_DIR = "page/"
PUBLISH_DIR = "publish/"
NOTAT_DIR = join(PUBLISH_DIR, "notater/")

def make_publish_dir():
    call(["mkdir", "-p", NOTAT_DIR])

def copy_page():
    copytree(PAGE_DIR, PUBLISH_DIR, dirs_exist_ok=True)

def call_latexes(cmd):
    notat = lambda x: join(NOTAT_DIR,x)
    cmd("TFE4101_Krets/", "Krets", notat("krets.pdf"))
    cmd("TMA4115_Matte3/", "Matte3", notat("matte3.pdf"))

def call(command, **kwargs):
    p = Popen(command, **kwargs)
    p.wait()
    if p.returncode != 0:
       error(f"command {' '.join(command)} failed with return code {p.returncode}")

def compile(folder, name, target):
    call(["latexmk", "-pdf", name+".tex"], cwd=folder)
    rename(join(folder,name+".pdf"), target)
    print(f" ==== Done! Moved {name}.pdf to {target} ==== ")

def clean_latex(folder, name, target):
    base = join(folder,name)
    extensions = ["aux", "fdb_latexmk", "fls", "log", "toc", "out"]
    call(["rm", "-f"] + [f"{base}.{ex}" for ex in extensions])

def error(msg, **kwargs):
    print(f"error: {msg}", **kwargs)
    exit(-1)

def print_help_text():
    print("Build script for compiling pdfs to a static site")
    print("Usage: ./build.py [command]")
    print()
    print("Commands:")
    print(f"all (default)    Build all latex and copy {PAGE_DIR} into {PUBLISH_DIR}")
    print(f"latex [filter]   Build all pdfs (optionally with name containing a filter)")
    print(f"ls               List all pdfs I can build")
    print(f"clean            Remove all build steps and output")
    exit()

if __name__ == "__main__":
    args = argv[1:]
    if "--help" in args:
        print_help_text()
    if args == [] or args == ["all"]:
        make_publish_dir()
        copy_page()
        call_latexes(compile)
    elif args[0] == "latex":
        if len(args) > 2:
            error("Too many args, see --help for usage")
        pattern = (args[1:2]+[""])[0]
        make_publish_dir()
        def compile_if_match(folder, name, target):
            if pattern in target:
                compile(folder, name, target)
        call_latexes(compile_if_match)
    elif args == ["ls"]:
        call_latexes(lambda folder,name,target: print(f"{target:<28} built from {join(folder,name)}.tex"))
    elif args == ["clean"]:
        call(["rm", "-rf", PUBLISH_DIR])
        call_latexes(clean_latex)
    else:
        error(f"Unrecognized command: '{' '.join(args)}'. See --help for usage")
