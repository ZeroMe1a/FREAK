# TODO: simp, mult, somar, sub

class Fractions:
    """
    Fractions calculations are made here.
    """

    def __init__(self) -> None:
        self.time = __import__("time")
        self.math = __import__("math")


    def simp(self, den: int, num: int) -> list:
        """
        Simplify fractions
        """        

        simplified = list()

        while self.math.gcd(den, num) > 1:
            gcd = self.math.gcd(den, num)
            simplified = [den / gcd, num / gcd]
            if den - gcd > 0 and num - gcd > 0:
                den -= gcd
                num -= gcd
            else:
                break
        return simplified

