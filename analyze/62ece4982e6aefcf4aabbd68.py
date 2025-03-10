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
    
    # Reverse to get the most significant digit first
    result_str = ''.join(reversed(result))
    
    # Apply padding if specified
    if padding is not None:
        if len(result_str) < padding:
            result_str = alphabet[0] * (padding - len(result_str)) + result_str
        elif len(result_str) > padding:
            raise ValueError("Padding is smaller than the length of the result.")
    
    return result_str