def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    import requests
    
    status_code = None
    error = None
    
    try:
        # Seleziona il metodo HTTP appropriato
        request_method = getattr(requests, method.lower())
        
        # Effettua la richiesta
        response = request_method(
            url,
            data=data,
            timeout=timeout,
            *args,
            **kwargs
        )
        
        # Salva il codice di stato
        status_code = response.status_code
        
        # Forza l'errore se status code non è 2xx
        response.raise_for_status()
            
    except requests.exceptions.RequestException as e:
        error = e
        
    except Exception as e:
        error = e
        
    return status_code, error