from passlib.hash import pbkdf2_sha256

def get_password_has(password):
    return pbkdf2_sha256.hash(password)

def verify_password(plainPassword, hashPassword):
    return pbkdf2_sha256.verify(plainPassword, hashPassword)