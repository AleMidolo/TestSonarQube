def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Analizar un enlace (href) de una imagen en partes compuestas.

    :param image_href: href de una imagen
    :returns: una tupla con el formato (image_id, netloc, use_ssl)
    :raises ValueError: Si el enlace no es valido o no puede ser analizado correctamente
    """
    from urllib.parse import urlparse
    
    if not image_href:
        raise ValueError("El enlace de imagen está vacío")
        
    try:
        # Analizar la URL
        parsed_url = urlparse(image_href)
        
        # Verificar el esquema
        if parsed_url.scheme not in ['http', 'https']:
            raise ValueError("Esquema de URL no válido")
            
        # Obtener el netloc
        netloc = parsed_url.netloc
        if not netloc:
            raise ValueError("URL sin dominio válido")
            
        # Determinar si usa SSL
        use_ssl = parsed_url.scheme == 'https'
        
        # Obtener el ID de la imagen del path
        path_parts = parsed_url.path.strip('/').split('/')
        if not path_parts[-1]:
            raise ValueError("URL no contiene ID de imagen")
            
        image_id = path_parts[-1]
        
        return (image_id, netloc, use_ssl)
        
    except Exception as e:
        raise ValueError(f"Error al analizar la URL de la imagen: {str(e)}")