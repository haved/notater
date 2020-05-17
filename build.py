#!/usr/bin/env python3

from subprocess import Popen
from os.path import join, isdir
from os import rename, mkdir

PUBLISH_DIR = "publish/"

def compile_all():
    if not isdir(PUBLISH_DIR):
        mkdir(PUBLISH_DIR)
    publish = lambda x: join(PUBLISH_DIR,x)
    compile("TFE4101_Krets/", "Krets", publish("krets.pdf"))
    compile("TMA4115_Matte3/", "Matte3", publish("matte3.pdf"))

def call(command, **kwargs):
    p = Popen(command, **kwargs)
    p.wait()
    if p.returncode != 0:
       print(f"Error: command {' '.join(command)} failed with return code {p.returncode}")
       exit(-1)     

def compile(folder, file, target):
    call(["latexmk", "-pdf", file+".tex"], cwd=folder)
    rename(join(folder,file+".pdf"), target)
    print(f" ==== Done! Moved {file}.pdf to {target} ==== ")

if __name__ == "__main__":
    compile_all()

