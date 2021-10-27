#! python3

import time
from colorama import Fore, Back


indent = 0
indent_increasing = True

while True:
    print(" " * indent, end=" ")
    print(f"{Back.RED + Fore.WHITE}*********\n\n")
    time.sleep(0.1)

    if indent_increasing:
        indent = indent + 1
        if indent == 15:
            indent_increasing = False

    else:
        indent = indent - 1
        if indent == 0:
            indent_increasing = True
