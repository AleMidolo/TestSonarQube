from typing import List

def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    Convert a string to a number, using the given alphabet.

    The input is assumed to have the most significant digit first.
    """
    base = len(alphabet)
    result = 0
    for char in string:
        result = result * base + alphabet.index(char)
    return result