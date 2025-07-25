def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    """
    Metodo di supporto per inviare un documento tramite POST.

    Gli ulteriori parametri ``*args`` e ``**kwargs`` saranno passati a ``requests.post``.

    :arg url: URL completo a cui inviare, incluso il protocollo  
    :arg data: Dizionario (sarà codificato come form), bytes o oggetto simile a un file da inviare nel corpo della richiesta  
    :arg timeout: Secondi di attesa per la risposta (predefinito: 10)  
    :arg method: Metodo da utilizzare, predefinito: post  
    :returns: Tupla contenente il codice di stato (int o None) e l'errore (istanza della classe di eccezione o None)
    """
    import requests
    
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
        
        # Restituisce il codice di stato e None come errore
        return response.status_code, None
        
    except requests.exceptions.RequestException as e:
        # In caso di errore, restituisce None come codice di stato e l'eccezione
        return None, e
    except Exception as e:
        # Gestisce altri possibili errori
        return None, e