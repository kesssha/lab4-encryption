from validation import validate_request


def process_text(text, key, mode):
    """
    Шифрует или расшифровывает текст
    методом Цезаря.
    """

    validate_request(text, key, mode)

    result = []

    shift = key if mode == "encrypt" else -key

    for char in text:

        if "a" <= char <= "z":
            new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))

        elif "A" <= char <= "Z":
            new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))

        else:
            new_char = char

        result.append(new_char)

    return "".join(result)


def encrypt(text, key):
    """Шифрование текста."""
    return process_text(text, key, "encrypt")


def decrypt(text, key):
    """Расшифрование текста."""
    return process_text(text, key, "decrypt")
