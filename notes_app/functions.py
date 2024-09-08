from notes_app import bcrypt

def HashPassword(password: str) -> str:
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    return hashed_password

def CheckPasswordHash(hash_password: str, password: bytes) -> bool:
    check = bcrypt.check_password_hash(hash_password, password)
    return check