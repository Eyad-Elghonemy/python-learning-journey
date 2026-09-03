# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Modules vs Packages
# [2] External Packages Downloaded From internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package And Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages And Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/refrence/pip_install/"
# ------------------------------------------

import termcolor

import pyfiglet

print(dir(pyfiglet))

# print(pyfiglet.figlet_format("Ali"))

# print(termcolor.colored("Ali", color= "yellow"))

for i in range(1, 20):
    
    print(" ")

print(termcolor.colored(pyfiglet.figlet_format("BEDO"), color= "green"))


for i in range(1, 20):
    
    print(" ")