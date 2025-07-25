def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    # Handle special case of 0
    if number == 0:
        result = alphabet[0]
        if padding:
            result = alphabet[0] * padding
        return result
        
    # Convert number to string using the provided alphabet
    base = len(alphabet)
    result = []
    
    # Convert to the desired base
    n = abs(number)
    while n:
        n, remainder = divmod(n, base)
        result.append(alphabet[remainder])
    
    # Handle negative numbers
    if number < 0:
        result.append('-')
        
    # Reverse the string since we built it from least significant digit
    result.reverse()
    
    # Add padding if needed
    if padding:
        while len(result) < padding:
            result.insert(0, alphabet[0])
            
    return ''.join(result)