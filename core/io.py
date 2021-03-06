from colorama import Fore

def get_fractions() -> list:
    fractions = list()
    while len(fractions) < 2:
        try:
            fractions.append(
                list(
                    map(int, 
                        input(Fore.GREEN + f"Fraction {len(fractions) + 1} " + Fore.RESET).split())
                )
            )
        except ValueError:
            return -1
    return fractions
    