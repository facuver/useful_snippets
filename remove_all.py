#### RUN ON MICROPYTHON BOARD
#### WILL DELETE ALL FILES

import os


def remove_recursive(dir):
    for i in os.ilistdir(dir):
        path = dir + "/" + i[0]
        if i[1] == 0x8000:
            print(f"{path} file removed ")
            os.remove(path)
        else:   #is dir
            print(f"{path} dir removed ")
            remove_recursive(path)
            os.rmdir(path)
        
    

remove_recursive("./")
