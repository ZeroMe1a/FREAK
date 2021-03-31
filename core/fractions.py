"""Fraction data type implementation."""


class Fraction:
    """
    Fraction data type.

    num -- fraction numerator
    den -- fraction denominator (den != 0)
    """

    def __init__(self, num: int, den: int):
        """__init__ bound method for fractions."""
        if den == 0:
            raise ValueError("Denominator must be different from 0.")
        self.num = num
        self.den = den
        self.__math = __import__("math")


    def __mul__(self, fraction):
        """__mul__ bound method for fractions."""
        return Fraction(self.num * fraction.num,
                        self.den * fraction.den)


    def __truediv__(self, fraction):
        """__truediv__ bound method for fractions."""
        return Fraction(self.num * fraction.den,
                        self.den * fraction.num)


    def __add__(self, fraction):
        """__add__ bound method for fractions."""
        if self.den == fraction.den:
            return Fraction(self.num + fraction.num,
                            self.den)
        else:
            lcm = self.__math.lcm(self.den, fraction.den)
            return Fraction(
                        ((lcm / self.den) * self.num) + ((lcm / fraction.den) * fraction.den),
                        lcm
                    )


    def __sub__(self, fraction):
        """__sub__ bound method for fractions."""
        if self.den == fraction.den:
            return Fraction(self.num - fraction.num,
                            self.den)
        else:
            lcm = self.__math.lcm(self.den, fraction.den)
            return Fraction(
                        ((lcm / self.den) * self.num) - ((lcm / fraction.den) * fraction.num),
                        lcm
                    )


    def __eq__(self, fraction):
        """__eq__ bound method for fractions."""
        return True if (self.simplify().num == fraction.simplify().num
                    and self.simplify().den == fraction.simplify().den) else False


    def __repr__(self):
            """__repr__ bound method for fractions."""
            return f"""Fraction(num={self.num}, den={self.den})"""


    def simplify(self):
        """Simplify the fraction object."""
        return Fraction(self.num / self.__math.gcd(int(self.num), int(self.den)),
                        self.den / self.__math.gcd(int(self.num), int(self.den)))


    def to_ratio(self):
        """Rational fraction representation."""
        return self.num / self.den

