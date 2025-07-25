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
        if method.lower() == "post":
            response = requests.post(url, data=data, timeout=timeout, *args, **kwargs)
        else:
            raise ValueError("Método no soportado: {}".format(method))

        return response.status_code, None
    except Exception as e:
        return None, e