def popular_words(text: str, words: list[str]) -> dict[str, int]:
    """
    Функція рахує, скільки разів кожне слово зі списку words зустрічається в тексті text.
    Пошук виконується без урахування регістру.
    """
    text = text.lower().split()
    return dict(map(lambda w: (w, text.count(w)), words))


assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']
) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')
