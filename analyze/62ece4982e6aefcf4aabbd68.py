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
    
    result.reverse()
    result_str = ''.join(result)
    
    if padding is not None:
        result_str = result_str.zfill(padding)
    
    return result_str