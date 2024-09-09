from encryption import encrypt

def decrypt(text, shift):
    return encrypt(text, -shift)

