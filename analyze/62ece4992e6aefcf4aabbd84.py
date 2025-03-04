def es_ipv4(objetivo):
    """
    Probar si es una dirección IPv4 o no
    """
    # Dividir la cadena por puntos
    octetos = objetivo.split('.')
    
    # Una IPv4 debe tener exactamente 4 octetos
    if len(octetos) != 4:
        return False
        
    # Verificar cada octeto
    for octeto in octetos:
        # Verificar que sea un número
        if not octeto.isdigit():
            return False
            
        # Convertir a entero
        num = int(octeto)
        
        # Verificar rango válido (0-255)
        if num < 0 or num > 255:
            return False
            
        # Verificar que no tenga ceros a la izquierda
        if len(octeto) > 1 and octeto[0] == '0':
            return False
            
    return True