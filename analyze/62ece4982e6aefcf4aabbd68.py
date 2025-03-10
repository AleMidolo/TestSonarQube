from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    '''
    Converti un numero in una stringa utilizzando l'alfabeto fornito.

    L'output avrà la cifra più significativa per prima.
    '''
    if number == 0:
        return alphabet[0] if not padding else alphabet[0] * padding
    
    base = len(alphabet)
    result = []
    
    while number > 0:
        remainder = number % base
        result.append(alphabet[remainder])
        number = number // base
    
    result.reverse()
    
    if padding:
        while len(result) < padding:
            result.insert(0, alphabet[0])
    
    return ''.join(result)