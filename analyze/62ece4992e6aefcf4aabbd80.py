import os

def remove_ending_os_sep(input_list):
    """
    Itera sobre una lista de cadenas y elimina los caracteres separadores de ruta del sistema operativo al final.

    Cada cadena se verifica para determinar si su longitud es mayor que uno y si el último
    carácter es el separador de ruta. Si es así, se elimina el carácter separador de ruta.

    Argumentos:
        input_list: lista de cadenas

    Devuelve:
        Lista procesada de cadenas

    Excepciones:
        TypeError
    """
    if not isinstance(input_list, list):
        raise TypeError("El argumento debe ser una lista.")
    
    processed_list = []
    for item in input_list:
        if not isinstance(item, str):
            raise TypeError("Todos los elementos de la lista deben ser cadenas.")
        
        if len(item) > 1 and item.endswith(os.sep):
            processed_list.append(item[:-1])
        else:
            processed_list.append(item)
    
    return processed_list