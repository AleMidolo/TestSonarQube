from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    base = len(alphabet)
    if base == 0:
        raise ValueError("Alphabet must not be empty")
    
    result = []
    while number > 0:
        remainder = number % base
        result.append(alphabet[remainder])
        number = number // base
    
    if not result:
        result.append(alphabet[0])
    
    result.reverse()
    
    result_str = ''.join(result)
    
    if padding is not None:
        if padding < len(result_str):
            raise ValueError("Padding must be greater than or equal to the length of the result")
        result_str = result_str.rjust(padding, alphabet[0])
    
    return result_str