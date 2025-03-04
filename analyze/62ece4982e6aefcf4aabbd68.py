def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    # Handle negative numbers
    if number < 0:
        raise ValueError("Negative numbers are not supported")
        
    # Handle zero case
    if number == 0:
        result = alphabet[0]
        if padding:
            result = alphabet[0] * padding
        return result
        
    # Convert number to string using given alphabet
    base = len(alphabet)
    result = []
    
    while number > 0:
        number, remainder = divmod(number, base)
        result.append(alphabet[remainder])
    
    # Reverse to get most significant digit first
    result.reverse()
    
    # Add padding if needed
    if padding:
        while len(result) < padding:
            result.insert(0, alphabet[0])
            
    return ''.join(result)