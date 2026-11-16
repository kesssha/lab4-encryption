import pytest

from cipher import encrypt, decrypt

def test_encrypt():
    assert encrypt("ABC", 3) == "DEF"

def test_decrypt():
    assert decrypt("DEF", 3) == "ABC"

def test_encrypt_lowercase():
    assert encrypt("abc", 3) == "def"

def test_encrypt_uppercase():
    assert encrypt("XYZ", 3) == "ABC"

def test_decrypt_lowercase():
    assert decrypt("def", 3) == "abc"

def test_preserve_symbols():
    assert encrypt("Hello 123!", 3) == "Khoor 123!"

def test_preserve_case():
    assert encrypt("AbC", 2) == "CdE"

def test_encrypt_russian_text():
    assert encrypt("Привет!", 3) == "Привет!"

def test_round_trip():
    original = "Hello World!"
    encrypted = encrypt(original, 5)
    decrypted = decrypt(encrypted, 5)

    assert decrypted == original

def test_invalid_encrypt():
    with pytest.raises(ValueError):
        encrypt("", 3)

def test_invalid_decrypt():
    with pytest.raises(ValueError):
        decrypt("Hello", 0)