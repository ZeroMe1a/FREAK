from os import name, system
from string import Template
from colorama import *

init(autoreset=True)

# colors avaiable:

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

def cls():
	if name == 'nt':
		_ = 'cls'
	else:
		_ = 'clear'
	system(_)

title = Template(Fore.YELLOW+"""
███████╗██████╗ ███████╗ █████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔══██╗██║ ██╔╝
█████╗  ██████╔╝█████╗  ███████║█████═╝ 
██╔══╝  ██╔══██╗██╔══╝  ██╔══██║██╔═██╗ 
██║     ██║  ██║███████╗██║  ██║██║ ╚██╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝"""+Fore.CYAN+"  $sub\n\n")