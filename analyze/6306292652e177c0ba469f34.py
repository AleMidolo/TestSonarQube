def fetch_content_type(url: str) -> Optional[str]:
    """
    Obtén el encabezado HEAD de la URL remota para determinar el tipo de contenido.
    """
    import requests
    from typing import Optional
    
    try:
        # Realizar solicitud HEAD para obtener solo los encabezados
        response = requests.head(url, allow_redirects=True)
        
        # Obtener el content-type del encabezado
        content_type = response.headers.get('content-type')
        
        # Si existe content-type, retornarlo. Si no, retornar None
        if content_type:
            return content_type.split(';')[0].strip()
        return None
        
    except requests.RequestException:
        # En caso de error en la solicitud, retornar None
        return None