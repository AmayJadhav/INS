import hmac
import hashlib

def generate_mac(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()

def verify_mac(key, message, mac):
    return hmac.new(key, message, hashlib.sha256).hexdigest() == mac

# Example usage
key = b'secret_key'
message = b'Hello, World!'

mac = generate_mac(key, message)
print(f"Generated MAC: {mac}")

is_valid = verify_mac(key, message, mac)
print(f"MAC is valid: {is_valid}")
