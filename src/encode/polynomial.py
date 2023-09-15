from encode.utils import gf_multiply, gf_power


class GFPolynomial:
    def __init__(self, coeffs: list):
        # All coefficients are assumed to be in [0, 255]
        self.degree = len(coeffs) - 1
        self.coeffs = coeffs

    @staticmethod
    def typecheck(p1, p2):
        if isinstance(p2, int):
            p2 = GFPolynomial([0] * p1.degree + [p2])

        elif isinstance(p2, GFPolynomial):
            if p1.degree > p2.degree:
                p2.coeffs = [0] * (p1.degree - p2.degree) + p2.coeffs
            elif p2.degree > p1.degree:
                p1.coeffs = [0] * (p2.degree - p1.degree) + p1.coeffs

        elif not isinstance(p2, GFPolynomial):
            raise TypeError

        return p1, p2

    def __repr__(self):
        poly = []
        for i, coeff in enumerate(self.coeffs[::-1]):
            if coeff == 0:
                pass
            elif i == 0:
                poly.append(str(coeff))
            elif i == 1 and coeff == 1:
                poly.append("x")
            elif i == 1 and coeff != 1:
                poly.append(f"{coeff}x")
            elif coeff == 1:
                poly.append(f"x^{i}")
            else:
                poly.append(f"{coeff}x^{i}")

        return (" + ").join(poly[::-1])

    def __add__(self, other):
        p1, p2 = self.typecheck(self, other)

        result = []
        for i in range(len(p1.coeffs)):
            result.append(abs(p1.coeffs[i]) ^ abs(p2.coeffs[i]))

        return GFPolynomial(result)

    def __sub__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        result = [0] * (self.degree + other.degree + 1)

        for i in range(self.degree + 1):
            for j in range(other.degree + 1):
                if 0 not in [self.coeffs[i], other.coeffs[j]]:
                    result[i+j] ^= gf_multiply(self.coeffs[i], other.coeffs[j])

        return GFPolynomial(result)

    def __mod__(self, other):
        # Assumes `other` is a monic polynomial.
        if self.degree < other.degree:
            return other

        diff = (self.degree - other.degree)
        dividend = self.coeffs

        for _ in range(diff+1):
            divisor = other.coeffs + [0] * diff
            temp = [gf_multiply(dividend[0], d) for d in divisor]
            dividend = (GFPolynomial(dividend) - GFPolynomial(temp)).coeffs[1:]
            diff -= 1

        return dividend

    def __call__(self, x):
        eval_value = 0
        for pow, c in enumerate(self.coeffs[::-1]):
            eval_value ^= gf_multiply(c, gf_power(x, pow))
        return eval_value
