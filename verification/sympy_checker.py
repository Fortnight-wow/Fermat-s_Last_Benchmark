"""
Symbolic verification utilities.

Future versions will compare mathematical expressions using SymPy.
"""

try:
    import sympy as sp
except ImportError:
    sp = None


if __name__ == '__main__':
    print('SymPy checker ready.')