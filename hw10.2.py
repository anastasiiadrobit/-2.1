def first_word(text: str) -> str:
    """
    Повертає перше слово з рядка.

    Заміщує крапки та коми пробілами і розбиває рядок на слова.
    Якщо рядок порожній або слів немає, повертає порожній рядок.

    Args:
        text (str): Рядок, з якого потрібно взяти перше слово.

    Returns:
        str: Перше слово рядка або порожній рядок.
    """
    text = text.replace('.', ' ').replace(',', ' ')
    words = text.split()
    return words[0] if words else ''


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')

