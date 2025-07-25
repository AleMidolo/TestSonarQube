def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    Convertire una stringa in un numero, utilizzando l'alfabeto fornito.  
    
    Si assume che l'input abbia la cifra più significativa per prima.
    """
    result = 0
    base = len(alphabet)
    
    for char in string:
        # Moltiplica il risultato corrente per la base e aggiungi il valore della cifra corrente
        digit_value = alphabet.index(char)
        result = result * base + digit_value
        
    return result