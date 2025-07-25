from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    """
    Convert a number to a string, using the given alphabet.

    The output has the most significant digit first.
    """
    if number < 0:
        raise ValueError("Number must be non-negative.")
    
    base = len(alphabet)
    if base == 0:
        raise ValueError("Alphabet must not be empty.")
    
    result = []
    while number > 0:
        number, remainder = divmod(number, base)
        result.append(alphabet[remainder])
    
    if not result:
        result.append(alphabet[0])
    
    result.reverse()
    
    if padding is not None:
        if padding < len(result):
            raise ValueError("Padding must be greater than or equal to the length of the result.")
        result = [alphabet[0]] * (padding - len(result)) + result
    
    return ''.join(result)