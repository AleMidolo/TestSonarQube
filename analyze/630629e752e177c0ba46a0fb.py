def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    """
    Método auxiliar para enviar un documento mediante POST.

    Los parámetros adicionales ``*args`` y ``**kwargs`` se pasarán a ``requests.post``.

    :arg url: URL completa a la que se enviará, incluyendo el protocolo  
    :arg data: Diccionario (se codificará como formulario), bytes o un objeto similar a un archivo que se enviará en el cuerpo  
    :arg timeout: Segundos a esperar por la respuesta (por defecto 10)  
    :arg method: Método a utilizar, por defecto es POST  
    :returns: Tupla que contiene el código de estado (int o None) y el error (instancia de la clase de excepción o None)  
    """
    import requests
    
    try:
        # Get the appropriate request method
        request_method = getattr(requests, method.lower())
        
        # Make the request
        response = request_method(
            url,
            data=data,
            timeout=timeout,
            *args,
            **kwargs
        )
        
        # Return status code and None for error
        return response.status_code, None
        
    except requests.exceptions.RequestException as e:
        # Return None for status code and the exception
        return None, e
    except Exception as e:
        # Return None for status code and the exception for any other errors
        return None, e