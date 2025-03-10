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
    
    result = []
    while number > 0:
        remainder = number % base
        result.append(alphabet[remainder])
        number = number // base
    
    if not result:
        result.append(alphabet[0])
    
    result.reverse()
    
    if padding is not None:
        while len(result) < padding:
            result.insert(0, alphabet[0])
    
    return ''.join(result)