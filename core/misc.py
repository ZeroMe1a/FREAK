from os import name, system
from string import Template
from colorama import *

init(autoreset=True)


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
