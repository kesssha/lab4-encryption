import pytest

from validation import validate_request

@pytest.mark.parametrize(
    "text, key, mode, expected",
    [
        ("Hello", 3, "encrypt", True),
        ("", 3, "encrypt", False),
        ("Hello", 0, "encrypt", False),
        ("Hello", 3, "unknown", False),
        ("", 0, "encrypt", False),
        ("", 3, "unknown", False),
        ("Hello", 0, "unknown", False),
        ("", 0, "unknown", False),
    ]
)
def test_combinatorial_conditions(text, key, mode, expected):

    if expected:
        assert validate_request(text, key, mode) is True
    else:
        with pytest.raises(ValueError):
            validate_request(text, key, mode)

def test_boolean_key():
    with pytest.raises(ValueError):
        validate_request("Hello", True, "encrypt")

def test_invalid_text_type():
    with pytest.raises(ValueError):
        validate_request(None, 3, "encrypt")

def test_key_too_large():
    with pytest.raises(ValueError):
        validate_request("Hello", 26, "encrypt")

def test_valid_decrypt_mode():
    assert validate_request("Hello", 3, "decrypt") is True