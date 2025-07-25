def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    # Handle negative numbers
    if number < 0:
        raise ValueError("Number must be non-negative")
        
    # Handle zero case
    if number == 0:
        result = alphabet[0]
        if padding:
            result = alphabet[0] * padding
        return result
        
    base = len(alphabet)
    digits = []
    
    # Convert to the desired base
    while number:
        digits.append(alphabet[number % base])
        number //= base
        
    # Reverse to get most significant digit first
    result = ''.join(digits[::-1])
    
    # Add padding if needed
    if padding:
        result = alphabet[0] * (padding - len(result)) + result if len(result) < padding else result
        
    return result