from typing import Union

def identify_request(request: Union[str, dict]) -> bool:
    """
    Intente identificar si esta es una solicitud de Matrix.
    
    Args:
        request: Puede ser una cadena o un diccionario que representa la solicitud.
    
    Returns:
        bool: True si la solicitud es de Matrix, False en caso contrario.
    """
    if isinstance(request, str):
        # Verificar si la cadena contiene indicadores de Matrix
        return "matrix" in request.lower()
    elif isinstance(request, dict):
        # Verificar si el diccionario contiene claves específicas de Matrix
        return any(key.lower() == "matrix" for key in request.keys())
    else:
        return False