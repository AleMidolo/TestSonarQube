from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    """
    Convert a number to a string using the given alphabet.
    The most significant digit will be first in the output.
    """
    if number < 0:
        raise ValueError("Number must be non-negative.")
    
    base = len(alphabet)
    if base == 0:
        raise ValueError("Alphabet must not be empty.")
    
    if number == 0:
        return alphabet[0] if padding is None else alphabet[0].rjust(padding, alphabet[0])
    
    result = []
    while number > 0:
        remainder = number % base
        result.append(alphabet[remainder])
        number = number // base
    
    result.reverse()
    
    output = ''.join(result)
    
    if padding is not None:
        output = output.rjust(padding, alphabet[0])
    
    return output