from utils import lookup_log, lookup_antilog


class GFPolynomial:
    def __init__(self, coeffs: list):
        # All coeffecients are assumed to be in [0, 255]
        self.degree = len(coeffs) - 1
        self.coeffs = coeffs
        self.irrd_poly_coeff = [1, 0, 0, 0, 1, 1, 1, 1, 0]

    @staticmethod
    def _typecheck(p1, p2):
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

    @staticmethod
    def gf_multiply(c1, c2):
        return lookup_antilog[(lookup_log[c1] + lookup_log[c2]) % 255]

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
        p1, p2 = self._typecheck(self, other)

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
                result[i+j] ^= self.gf_multiply(self.coeffs[i], other.coeffs[j])

        return GFPolynomial(result)



if __name__ == "__main__":
    res = GFPolynomial([1, 1])

    for i in range(1, 7):
        res *= GFPolynomial([1, 2**i])

    print(res)