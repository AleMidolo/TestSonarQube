from typing import List

def string_to_int(string: str, alphabet: List[str]) -> int:
    base = len(alphabet)
    value = 0
    for char in string:
        value = value * base + alphabet.index(char)
    return value