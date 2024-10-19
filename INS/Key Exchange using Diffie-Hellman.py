if __name__ == '__main__':
    P = 23
    G = 9
    print(f"The Value of P is {P}")
    print(f"The Value of G is {G}")

    # Alice's secret key
    a = 4
    print(f"Secret Number for Alice is: {a}")

    # Alice's public key
    x = pow(G, a, P)

    # Bob's secret key
    b = 6
    print(f"Secret Number for Bob is: {b}")

    # Bob's public key
    y = pow(G, b, P)

    # Shared secret key for Alice
    ka = pow(y, a, P)

    # Shared secret key for Bob
    kb = pow(x, b, P)

    print(f"Secret Key for the Alice is: {ka}")
    print(f"Secret Key for the Bob is: {kb}")
