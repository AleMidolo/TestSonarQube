def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    # Manejo de caso especial para número 0
    if number == 0:
        result = alphabet[0]
        if padding:
            result = result.rjust(padding, alphabet[0])
        return result
        
    # Convertir el número usando el alfabeto dado
    base = len(alphabet)
    result = ""
    
    # Convertir número a la base del alfabeto
    n = abs(number)
    while n:
        result = alphabet[n % base] + result
        n //= base
        
    # Agregar signo negativo si es necesario
    if number < 0:
        result = '-' + result
        
    # Agregar padding si se especificó
    if padding:
        result = result.rjust(padding, alphabet[0])
        
    return result