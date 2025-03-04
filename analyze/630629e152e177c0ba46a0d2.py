def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Recupera e analizza un documento webfinger remoto di Diaspora.

    :arg handle: Handle remoto da recuperare  
    :returns: dict
    """
    import requests
    import json
    from urllib.parse import urlparse

    # Estrai il dominio dall'handle
    if '@' not in handle:
        raise ValueError("Handle non valido - deve contenere @")
        
    username, domain = handle.split('@')
    
    # Costruisci l'URL webfinger
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Recupera il documento webfinger
        response = requests.get(webfinger_url, timeout=10)
        response.raise_for_status()
        
        # Analizza il JSON
        webfinger_data = response.json()
        
        # Verifica che sia un documento webfinger valido
        if 'subject' not in webfinger_data:
            raise ValueError("Documento webfinger non valido")
            
        # Estrai i link e le proprietà rilevanti
        result = {
            'subject': webfinger_data['subject'],
            'aliases': webfinger_data.get('aliases', []),
            'links': {},
            'properties': {}
        }
        
        # Elabora i link
        for link in webfinger_data.get('links', []):
            if 'rel' in link and 'href' in link:
                result['links'][link['rel']] = link['href']
                
        # Elabora le proprietà
        for key, value in webfinger_data.get('properties', {}).items():
            result['properties'][key] = value
            
        return result
        
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Impossibile recuperare il webfinger: {str(e)}")
    except json.JSONDecodeError:
        raise ValueError("Documento webfinger non è JSON valido")