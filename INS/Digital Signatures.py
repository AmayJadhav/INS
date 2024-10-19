from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate RSA private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Serialize keys to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save keys to files
with open("private_key.pem", "wb") as f:
    f.write(private_pem)
with open("public_key.pem", "wb") as f:
    f.write(public_pem)

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

message = b"Hello, this is a signed message!"

# Sign the message
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Save the signature to a file
with open("signature.sig", "wb") as f:
    f.write(signature)

    from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

# Load the public key from file
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Load the signature from file
with open("signature.sig", "rb") as f:
    signature = f.read()

# Verify the signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid.")

