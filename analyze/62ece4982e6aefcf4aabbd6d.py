def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    Convertir una cadena a un número, utilizando el alfabeto dado.  
    
    Se asume que la entrada tiene el dígito más significativo primero.
    """
    result = 0
    base = len(alphabet)
    
    for char in string:
        # Multiplicar el resultado actual por la base y sumar el valor del nuevo dígito
        digit_value = alphabet.index(char)
        result = result * base + digit_value
        
    return result