# TODO: Implementar .simple(), plus, minus, div e operadores de comparação
class Fraction:
    """
    Fraction data type.

    num -- fraction numerator
    den -- fraction denominator
    """

    def __init__(self, num: int, den: int):
        """__init__ bound method for fractions."""
        self.num = num
        self.den = den

    
    def __mul__(self, fraction):
        """__mul__ bound method for fractions."""
        return Fraction(self.num * fraction.num,
                        self.den * fraction.den)

    def __repr__(self):
        """__repr__ bound method for fractions."""

        return f"""Fraction(num={self.num}, den={self.den})"""


    def __eq__(self, fraction):
        """__eq__ bound method for fractions."""
        return True if self.num == fraction.num and self.den == fraction.den else False

