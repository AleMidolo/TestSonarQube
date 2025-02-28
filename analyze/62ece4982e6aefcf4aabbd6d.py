from typing import List

def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    Convertir una cadena a un número, utilizando el alfabeto dado.  

    Se asume que la entrada tiene el dígito más significativo primero.
    """
    base = len(alphabet)
    result = 0
    for i, char in enumerate(string):
        value = alphabet.index(char)
        result = result * base + value
    return result