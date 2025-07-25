def string_to_int(string: str, alphabet: List[str]) -> int:
    base = len(alphabet)
    result = 0
    
    # Create a mapping of characters to their values
    char_to_val = {char: val for val, char in enumerate(alphabet)}
    
    # Process each character from left to right
    for char in string:
        # Multiply current result by base and add new digit
        result = result * base + char_to_val[char]
        
    return result