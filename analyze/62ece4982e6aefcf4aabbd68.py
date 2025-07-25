def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    # Handle 0 case
    if number == 0:
        result = alphabet[0]
        if padding:
            result = result.rjust(padding, alphabet[0])
        return result
        
    # Convert number to string using given alphabet
    base = len(alphabet)
    result = ""
    n = abs(number)
    
    while n:
        n, remainder = divmod(n, base)
        result = alphabet[remainder] + result
        
    # Add negative sign if needed
    if number < 0:
        result = '-' + result
        
    # Add padding if specified
    if padding:
        result = result.rjust(padding, alphabet[0])
        
    return result