from typing import Union

def identify_request(request: Union[str, dict]) -> bool:
    """
    Intente identificar si esta es una solicitud de Matrix.
    
    Args:
        request (Union[str, dict]): La solicitud a identificar, que puede ser un string o un diccionario.
    
    Returns:
        bool: True si la solicitud es de Matrix, False en caso contrario.
    """
    if isinstance(request, str):
        # Verificar si el string contiene indicadores de Matrix
        return "matrix" in request.lower()
    elif isinstance(request, dict):
        # Verificar si el diccionario contiene claves específicas de Matrix
        return any(key.lower() == "matrix" for key in request.keys())
    else:
        return False