from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    """
    संख्या को वर्णमाला का उपयोग करके स्ट्रिंग में परिवर्तित करें।
    आउटपुट में सबसे महत्वपूर्ण अंक पहले होगा।
    """
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    base = len(alphabet)
    if base == 0:
        raise ValueError("Alphabet list cannot be empty")
    
    result = []
    while number > 0:
        remainder = number % base
        result.append(alphabet[remainder])
        number = number // base
    
    if padding is not None:
        while len(result) < padding:
            result.append(alphabet[0])
    
    result.reverse()
    return ''.join(result)