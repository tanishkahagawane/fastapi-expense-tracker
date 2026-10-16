
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

password_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    """Hash a plain-text password using Argon2."""
    return password_hasher.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """Verify a plain-text password against its Argon2 hash."""
    try:
        return password_hasher.verify(
            hashed_password,
            plain_password
        )
    except (VerifyMismatchError, VerificationError):
        return False
