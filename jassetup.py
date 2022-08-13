from ensurepip import version
import py_compile
from sys import executable
from unicodedata import name
from cx_Freeze import setup, Executable

setup(name="object detection softwarejasmodel",
version= "0.1(used)",
description = "this object detects object in realtime",
execuatbles=[Executable("main.py")])


