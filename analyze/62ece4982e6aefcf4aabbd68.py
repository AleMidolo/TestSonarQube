from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    base = len(alphabet)
    result = []
    
    if number == 0:
        result.append(alphabet[0])
    
    while number > 0:
        number, remainder = divmod(number, base)
        result.append(alphabet[remainder])
    
    result.reverse()
    
    if padding is not None:
        result = ([''] * (padding - len(result))) + result
    
    return ''.join(result)