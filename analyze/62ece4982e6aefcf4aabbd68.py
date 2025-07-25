def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    # Handle special case of 0
    if number == 0:
        result = alphabet[0]
        if padding:
            result = result.rjust(padding, alphabet[0])
        return result
        
    # Convert number to string using the provided alphabet
    base = len(alphabet)
    result = ""
    
    # Convert to the desired base
    n = abs(number)
    while n:
        result = alphabet[n % base] + result
        n //= base
        
    # Add negative sign if needed
    if number < 0:
        result = '-' + result
        
    # Add padding if specified
    if padding:
        result = result.rjust(padding, alphabet[0])
        
    return result