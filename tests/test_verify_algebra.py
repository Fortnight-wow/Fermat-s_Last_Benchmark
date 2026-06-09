from verification.sympy.verify_algebra import verify_identity


def test_identity_true():
    assert verify_identity('(x+1)**2', 'x**2+2*x+1') is True
