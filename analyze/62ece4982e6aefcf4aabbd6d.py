def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    Convert a string to a number, using the given alphabet.
    
    The input is assumed to have the most significant digit first.
    """
    base = len(alphabet)
    result = 0
    
    # Create a mapping from characters to their values
    char_to_val = {char: i for i, char in enumerate(alphabet)}
    
    # Process each character from left to right
    for char in string:
        # Multiply current result by base and add new digit
        result = result * base + char_to_val[char]
        
    return result