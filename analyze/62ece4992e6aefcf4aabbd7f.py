def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Analizar un enlace (href) de una imagen en partes compuestas.

    :param image_href: href de una imagen
    :returns: una tupla con el formato (image_id, netloc, use_ssl)
    :raises ValueError: Si el enlace no es valido o no puede ser analizado correctamente
    """
    from urllib.parse import urlparse
    
    # Validar que el href no esté vacío
    if not image_href:
        raise ValueError("El href de la imagen está vacío")
        
    try:
        # Parsear la URL
        parsed = urlparse(image_href)
        
        # Validar que tenga un esquema y netloc
        if not parsed.scheme or not parsed.netloc:
            raise ValueError("URL inválida: debe contener esquema y dominio")
            
        # Obtener el netloc
        netloc = parsed.netloc
        
        # Determinar si usa SSL
        use_ssl = parsed.scheme == 'https'
        
        # Obtener el image_id del path
        # Asumimos que el último segmento del path es el id
        path_segments = parsed.path.split('/')
        image_id = path_segments[-1]
        
        if not image_id:
            raise ValueError("No se pudo extraer el ID de la imagen")
            
        return (image_id, netloc, use_ssl)
        
    except Exception as e:
        raise ValueError(f"Error al parsear la URL de la imagen: {str(e)}")