from sympy import isprime


def verify_twin_prime(p: int) -> bool:
    return isprime(p) and isprime(p + 2)


if __name__ == '__main__':
    sample = 11
    print(f'Twin prime check for {sample}:', verify_twin_prime(sample))
