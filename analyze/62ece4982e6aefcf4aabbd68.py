from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    '''
    Converti un numero in una stringa utilizzando l'alfabeto fornito.

    L'output avrà la cifra più significativa per prima.
    '''
    if number < 0:
        raise ValueError("Il numero deve essere non negativo.")
    
    base = len(alphabet)
    if base == 0:
        raise ValueError("L'alfabeto non può essere vuoto.")
    
    if number == 0:
        return alphabet[0] if padding is None else alphabet[0].rjust(padding, alphabet[0])
    
    result = []
    while number > 0:
        remainder = number % base
        result.append(alphabet[remainder])
        number = number // base
    
    result.reverse()
    
    result_str = ''.join(result)
    
    if padding is not None:
        result_str = result_str.rjust(padding, alphabet[0])
    
    return result_str