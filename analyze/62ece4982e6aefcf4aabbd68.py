from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    """
    Convierte un número a una cadena, utilizando el alfabeto proporcionado.  

    La salida tiene el dígito más significativo primero.
    """
    if number < 0:
        raise ValueError("El número debe ser no negativo.")
    
    base = len(alphabet)
    if base == 0:
        raise ValueError("El alfabeto no puede estar vacío.")
    
    if number == 0:
        return alphabet[0] if padding is None else alphabet[0].rjust(padding, alphabet[0])
    
    result = []
    while number > 0:
        remainder = number % base
        result.append(alphabet[remainder])
        number = number // base
    
    result.reverse()
    
    output = ''.join(result)
    
    if padding is not None:
        output = output.rjust(padding, alphabet[0])
    
    return output