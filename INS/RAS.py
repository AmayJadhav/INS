import random
from sympy import isprime, mod_inverse

# Generate a random prime number
def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

# Generate RSA keys
def generate_rsa_keys(bits=512):
    p, q = generate_prime(bits), generate_prime(bits)
    n, phi = p * q, (p - 1) * (q - 1)
    e = 65537  # Common choice for e
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

# Encrypt message using RSA
def rsa_encrypt(pub_key, message):
    n, e = pub_key
    msg_int = int.from_bytes(message.encode(), 'big')
    return pow(msg_int, e, n)

# Decrypt RSA-encrypted message
def rsa_decrypt(priv_key, cipher):
    n, d = priv_key
    msg_int = pow(cipher, d, n)
    return msg_int.to_bytes((msg_int.bit_length() + 7) // 8, 'big').decode()

# Main test
if __name__ == "__main__":
    public_key, private_key = generate_rsa_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("Enter message to encrypt: ")
    ciphertext = rsa_encrypt(public_key, message)
    print("Ciphertext:", ciphertext)

    decrypted_message = rsa_decrypt(private_key, ciphertext)
    print("Decrypted message:", decrypted_message)
