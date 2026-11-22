def validate_request(text, key, mode):
    """
    Проверяет корректность входных данных.
    """

    # Условие 1: текст должен быть строкой и не быть пустым
    text_ok = isinstance(text, str) and bool(text.strip())

    # Условие 2: ключ должен быть целым числом от 1 до 25
    key_ok = (
        isinstance(key, int) and not isinstance(key, bool) and 1 <= key <= 25
    )

    # Условие 3: режим должен быть допустимым
    mode_ok = mode in ("encrypt", "decrypt")

    # Проверка всех трёх условий
    if not (text_ok and key_ok and mode_ok):
        raise ValueError("Некорректные входные данные")

    return True
