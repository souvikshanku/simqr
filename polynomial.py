class GFPolynomial:
    def _init_(self, coeffs: list):
        self.degree = len(coeffs)
        self.coeffs = coeffs
        self.irrd_poly_coeff = [1, 0, 0, 0, 1, 1, 1, 1, 0]

    def _repr_(self):
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

    def _add_(self, other):
        if isinstance(other, int):
            other = GFPolynomial([0] * (self.degree - 1) + [other])

        elif isinstance(other, GFPolynomial):
            if self.degree > other.degree:
                other.coeffs = [0] * (self.degree - other.degree) + other.coeffs
            elif other.degree > self.degree:
                self.coeffs = [0] * (other.degree - self.degree) + self.coeffs

        elif not isinstance(other, GFPolynomial):
            raise TypeError

        resultant_coeffs = []
        for i in range(len(self.coeffs)):
            resultant_coeffs.append(abs(self.coeffs[i]) ^ abs(other.coeffs[i]))

        return GFPolynomial(resultant_coeffs)

    def _sub_(self, other):
        return self._add_(other)

    def _mul_(self, other):
        pass