#!/usr/bin/env python3

from subprocess import Popen
from os.path import join, isdir
from os import rename, mkdir

PAGE_DIR = "page/"
PUBLISH_DIR = "publish/"

def publish_dir():
    if not isdir(PUBLISH_DIR):
        mkdir(PUBLISH_DIR)

def copy_page():
    call(["cp", "-r", join(PAGE_DIR,"*"), PUBLISH_DIR])

def call_latexes(cmd):
    publish = lambda x: join(PUBLISH_DIR,x)
    cmd("TFE4101_Krets/", "Krets", publish("krets.pdf"))
    cmd("TMA4115_Matte3/", "Matte3", publish("matte3.pdf"))

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
    publish_dir()
    copy_page()
    call_latexes(compile)

