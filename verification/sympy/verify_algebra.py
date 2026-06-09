from sympy import simplify, sympify


def verify_identity(lhs: str, rhs: str) -> bool:
    return simplify(sympify(lhs) - sympify(rhs)) == 0


if __name__ == '__main__':
    print(verify_identity('(x+1)**2', 'x**2 + 2*x + 1'))
