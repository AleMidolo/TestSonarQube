def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    एक स्ट्रिंग को एक संख्या में बदलने का कार्य करता है, दिए गए वर्णमाला का उपयोग करके।

    इनपुट यह मानता है कि सबसे महत्वपूर्ण अंक (most significant digit) पहले है।
    """
    base = len(alphabet)
    result = 0
    
    # Create mapping of characters to their values
    char_to_val = {char: i for i, char in enumerate(alphabet)}
    
    # Process each character from left to right
    for char in string:
        # Multiply current result by base and add new digit
        result = result * base + char_to_val[char]
        
    return result