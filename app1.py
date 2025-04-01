from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
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
        return True
    except:
        return False

if __name__ == "__main__":
    # Generate RSA keys
    private_key, public_key = generate_keys()
    
    # Generate another set of keys to test invalid verification
    other_private_key, other_public_key = generate_keys()
    
    # Message to be signed
    message = b"Hello, RSA Signature!"
    
    # Sign the message
    signature = sign_message(private_key, message)
    print("Signature:", signature.hex())
    
    # Verify the signature with the correct public key
    is_valid = verify_signature(public_key, message, signature)
    print("Signature Valid with Correct Public Key:", is_valid)
    
    # Verify the signature with a modified message
    modified_message = b"Hello, Modified RSA Signature!"
    is_valid_modified = verify_signature(public_key, modified_message, signature)
    print("Signature Valid with Modified Message:", is_valid_modified)
    
    # Verify the signature with a different public key
    is_valid_different_key = verify_signature(other_public_key, message, signature)
    print("Signature Valid with Different Public Key:", is_valid_different_key)
