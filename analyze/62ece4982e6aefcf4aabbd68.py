from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    base = len(alphabet)
    if base < 2:
        raise ValueError("Alphabet must contain at least two characters")
    
    result = []
    while number > 0:
        result.append(alphabet[number % base])
        number //= base
    
    if padding is not None:
        while len(result) < padding:
            result.append(alphabet[0])  # Pad with the first character of the alphabet
    
    return ''.join(reversed(result)) if result else alphabet[0]