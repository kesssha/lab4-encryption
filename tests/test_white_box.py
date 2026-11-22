import pytest

from validation import validate_request


@pytest.mark.parametrize(
    "text, key, mode, expected",
    [
        ("Hello", 3, "encrypt", True),
        ("", 3, "encrypt", False),
        ("Hello", 0, "encrypt", False),
        ("Hello", 3, "unknown", False),
    ],
)
def test_decision_and_condition_coverage(text, key, mode, expected):
    if expected:
        assert validate_request(text, key, mode) is True
    else:
        with pytest.raises(ValueError):
            validate_request(text, key, mode)


def test_all_conditions_true():
    assert validate_request("Hello", 3, "encrypt") is True


def test_text_condition_false():
    with pytest.raises(ValueError):
        validate_request("", 3, "encrypt")


def test_key_condition_false():
    with pytest.raises(ValueError):
        validate_request("Hello", 0, "encrypt")


def test_mode_condition_false():
    with pytest.raises(ValueError):
        validate_request("Hello", 3, "unknown")
