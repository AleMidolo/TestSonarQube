from typing import List

def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    Convertire una stringa in un numero, utilizzando l'alfabeto fornito.  

    Si assume che l'input abbia la cifra più significativa per prima.
    """
    base = len(alphabet)
    num = 0
    for i, char in enumerate(string):
        power = len(string) - i - 1
        num += alphabet.index(char) * (base ** power)
    return num