from verification.sympy.verify_number_theory import verify_twin_prime


def test_valid_twin_prime():
    assert verify_twin_prime(11) is True


def test_invalid_twin_prime():
    assert verify_twin_prime(23) is False
