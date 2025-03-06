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
    
    result = []
    while number > 0:
        number, remainder = divmod(number, base)
        result.append(alphabet[remainder])
    
    if not result:
        result.append(alphabet[0])
    
    if padding is not None:
        while len(result) < padding:
            result.append(alphabet[0])
    
    return ''.join(reversed(result))