from core.fractions import *
from core.misc import *

# may god have mercy on my shitty code

# colors avaiable:

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

# ------------------------------------------------------

init(autoreset=True)

# ------------------------------------------------------



def opt1():
	cls()
	print(title.substitute(sub='Adding Fractions'))


	f1 = list(map(int, input(Fore.GREEN+'Fraction 1: ').split(' '))) 
	f2 = list(map(int, input(Fore.GREEN+'Fraction 2: ').split(' ')))

	r = add(f1, f2)
	s = simp([r[0], r[1]])

	print(Fore.CYAN+'\nResult: '+Fore.YELLOW+f'{r[0]}/{r[1]}')
	print(Fore.CYAN+'Simplified: '+Fore.YELLOW+f'{s[0]}/{s[1]}')
	print(Fore.CYAN+'Total Time (nano seconds): '+Fore.YELLOW+f'{r[2]+s[2]:0.2f}\n')

	input(Fore.GREEN+'Press enter to continue...')

	main_menu()


def opt2():
	cls()
	print(title.substitute(sub='Substracting Fractions'))

	f1 = list(map(int, input(Fore.GREEN+'Fraction 1: ').split(' '))) 
	f2 = list(map(int, input(Fore.GREEN+'Fraction 2: ').split(' ')))

	r = sub(f1, f2)
	s = simp([r[0], r[1]])

	print(Fore.CYAN+'\nResult: '+Fore.YELLOW+f'{r[0]}/{r[1]}')
	print(Fore.CYAN+'Simplified: '+Fore.YELLOW+f'{s[0]}/{s[1]}')
	print(Fore.CYAN+'Total Time (nano seconds): '+Fore.YELLOW+f'{r[2]+s[2]:0.2f}\n')

	input(Fore.GREEN+'Press enter to continue...')
	main_menu()


def opt3():
	cls()
	print(title.substitute(sub='Multiplying Fractions'))

	f1 = list(map(int, input(Fore.GREEN+'Fraction 1: ').split(' '))) 
	f2 = list(map(int, input(Fore.GREEN+'Fraction 2: ').split(' ')))

	r = mul(f1, f2)
	s = simp([r[0], r[1]])

	print(Fore.CYAN+'\nResult: '+Fore.YELLOW+f'{r[0]}/{r[1]}')
	print(Fore.CYAN+'Simplified: '+Fore.YELLOW+f'{s[0]}/{s[1]}\n')
	print(Fore.CYAN+'Total Time (nano seconds): '+Fore.YELLOW+f'{r[2]+s[2]:0.2f}\n')

	input(Fore.GREEN+'Press enter to continue...')
	main_menu()



# ------------------------------------------------------



def main_menu():
	cls()
	print(title.substitute(sub='Main Menu'))

	print(Fore.YELLOW+'[0] '+Fore.CYAN+'Quit')
	print(Fore.YELLOW+'[1] '+Fore.CYAN+'Add Fractions')
	print(Fore.YELLOW+'[2] '+Fore.CYAN+'Substract Fractions')
	print(Fore.YELLOW+'[3] '+Fore.CYAN+'Multiply Fractions')

	c = input(Fore.GREEN+'\n?: ')

	if c == '0': quit()

	elif c == '1': opt1()

	elif c == '2': opt2()

	elif c == '3': opt3()

	else:
		main_menu()



# ------------------------------------------------------

main_menu()
