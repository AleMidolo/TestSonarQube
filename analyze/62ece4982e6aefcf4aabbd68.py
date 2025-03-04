def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    # Manejo del caso especial cuando el número es 0
    if number == 0:
        result = alphabet[0]
        if padding:
            result = result.rjust(padding, alphabet[0])
        return result
        
    # Convertir el número usando el alfabeto dado
    base = len(alphabet)
    result = ""
    
    # Convertir el número a la base del alfabeto
    n = abs(number)
    while n:
        result = alphabet[n % base] + result
        n //= base
        
    # Agregar el signo negativo si es necesario
    if number < 0:
        result = '-' + result
        
    # Agregar padding si se especifica
    if padding:
        if number < 0:
            # Si es negativo, el padding va después del signo
            result = '-' + result[1:].rjust(padding, alphabet[0])
        else:
            result = result.rjust(padding, alphabet[0])
            
    return result