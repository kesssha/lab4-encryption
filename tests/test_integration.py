import pytest

from cipher import encrypt, decrypt


def test_full_encryption_cycle():
    original_text = "Hello World!"

    encrypted_text = encrypt(original_text, 3)
    decrypted_text = decrypt(encrypted_text, 3)

    assert encrypted_text == "Khoor Zruog!"
    assert decrypted_text == original_text


def test_validation_and_encryption_integration():
    original_text = "Python"

    encrypted_text = encrypt(original_text, 5)

    assert encrypted_text == "Udymts"


def test_validation_and_decryption_integration():
    encrypted_text = "Udymts"

    decrypted_text = decrypt(encrypted_text, 5)

    assert decrypted_text == "Python"


def test_invalid_data_integration():
    with pytest.raises(ValueError):
        encrypt("", 3)


def test_invalid_key_integration():
    with pytest.raises(ValueError):
        decrypt("Hello", 0)


def test_symbols_integration():
    original_text = "Hello 123!"

    encrypted_text = encrypt(original_text, 3)
    decrypted_text = decrypt(encrypted_text, 3)

    assert encrypted_text == "Khoor 123!"
    assert decrypted_text == original_text
