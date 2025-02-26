from typing import List

def string_to_int(string: str, alphabet: List[str]) -> int:
    base = len(alphabet)
    num = 0
    for char in string:
        num = num * base + alphabet.index(char)
    return num