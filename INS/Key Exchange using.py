from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Generate some parameters. These can be reused.
parameters = dh.generate_parameters(generator=2, key_size=2048)

# Serialize parameters
param_pem = parameters.parameter_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.ParameterFormat.PKCS3
)

# Save the parameters to a file
with open("dh_parameters.pem", "wb") as f:
    f.write(param_pem)

# Load parameters
with open("dh_parameters.pem", "rb") as f:
    param_pem = f.read()
parameters = dh.DHParameterNumbers.load_pem_parameters(param_pem)

# Generate private key for party A
private_key_a = parameters.generate_private_key()
public_key_a = private_key_a.public_key()

# Serialize party A's public key
public_pem_a = public_key_a.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save party A's public key to a file
with open("public_key_a.pem", "wb") as f:
    f.write(public_pem_a)

# Generate private key for party B
private_key_b = parameters.generate_private_key()
public_key_b = private_key_b.public_key()

# Serialize party B's public key
public_pem_b = public_key_b.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save party B's public key to a file
with open("public_key_b.pem", "wb") as f:
    f.write(public_pem_b)

# Load public key for party B
with open("public_key_b.pem", "rb") as f:
    public_key_b = serialization.load_pem_public_key(f.read())

# Party A generates the shared secret using their private key and party B's public key
shared_key_a = private_key_a.exchange(public_key_b)

# Load public key for party A
with open("public_key_a.pem", "rb") as f:
    public_key_a = serialization.load_pem_public_key(f.read())

# Party B generates the shared secret using their private key and party A's public key
shared_key_b = private_key_b.exchange(public_key_a)

# Verify that both shared keys are the same
assert shared_key_a == shared_key_b
print("Shared key:", shared_key_a.hex())
