from typing import List

def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    Convertire una stringa in un numero, utilizzando l'alfabeto fornito.  

    Si assume che l'input abbia la cifra più significativa per prima.
    """
    base = len(alphabet)
    value = 0
    for char in string:
        value = value * base + alphabet.index(char)
    return value