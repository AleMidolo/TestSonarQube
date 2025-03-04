def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    # Handle negative numbers
    if number < 0:
        raise ValueError("Number must be non-negative")
        
    # Handle zero case
    if number == 0:
        result = alphabet[0]
        if padding:
            result = result * padding
        return result
        
    base = len(alphabet)
    result = []
    
    # Convert number to string using the provided alphabet
    while number > 0:
        digit = number % base
        result.append(alphabet[digit])
        number //= base
        
    # Reverse the result since we want most significant digit first
    result.reverse()
    
    # Add padding if needed
    if padding and len(result) < padding:
        result = [alphabet[0]] * (padding - len(result)) + result
        
    return ''.join(result)