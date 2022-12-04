### require mpy-cross 
### compile all file to bytecode and save it to the ./dist folder 



import mpy_cross
from distutils.dir_util import copy_tree
import time

import os
SRC_PATH = "./"
DIST_PATH = "./dist"
def recursive_compuie(path):
    for f in os.scandir(path):
        if f.is_dir():
            print(f.path)
            recursive_compuie(f.path)
        else:
            print(f.path)
            if f.name.endswith(".py"):
                mpy_cross.run(f.path)
                time.sleep(0.01)
                os.remove(f.path)

copy_tree(SRC_PATH,DIST_PATH)
recursive_compuie(DIST_PATH)
