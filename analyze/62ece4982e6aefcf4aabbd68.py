from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    base = len(alphabet)
    if base < 2:
        raise ValueError("Alphabet must have at least two characters")
    
    if number == 0:
        result = alphabet[0]
    else:
        result = ""
        while number > 0:
            result = alphabet[number % base] + result
            number //= base
    
    if padding is not None:
        result = result.rjust(padding, alphabet[0])
    
    return result