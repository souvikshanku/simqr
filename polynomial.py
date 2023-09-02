class GFPolynomial:
    def __init__(self, coeffs: list):
        self.degree = len(coeffs)
        self.coeffs = coeffs
        self.irrd_poly_coeff = [1, 0, 0, 0, 1, 1, 1, 1, 0]

    @staticmethod
    def _typecheck(p1, p2):
        if isinstance(p2, int):
            p2 = GFPolynomial([0] * (p1.degree - 1) + [p2])

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
        p1, p2 = self._typecheck(self, other)

        result = []
        for i in range(len(p1.coeffs)):
            result.append(abs(p1.coeffs[i]) ^ abs(p2.coeffs[i]))

        return GFPolynomial(result)

    def __sub__(self, other):
        return self._add_(other)

    def __mul__(self, other):
        pass