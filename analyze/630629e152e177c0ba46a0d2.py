def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Recupera e analizza un documento webfinger remoto di Diaspora.

    :arg handle: Handle remoto da recuperare  
    :returns: dict
    """
    import requests
    import json
    from urllib.parse import urlparse

    # Verifica che l'handle sia valido
    if '@' not in handle:
        raise ValueError("Handle non valido - deve contenere @")

    username, domain = handle.split('@', 1)
    
    # Costruisci l'URL webfinger
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Recupera il documento webfinger
        response = requests.get(webfinger_url, timeout=10)
        response.raise_for_status()
        
        # Analizza la risposta JSON
        webfinger_data = response.json()
        
        # Estrai le informazioni rilevanti
        result = {
            'handle': handle,
            'username': username,
            'domain': domain,
            'links': {}
        }
        
        # Analizza i link nel documento webfinger
        if 'links' in webfinger_data:
            for link in webfinger_data['links']:
                rel = link.get('rel', '')
                href = link.get('href', '')
                type_ = link.get('type', '')
                
                result['links'][rel] = {
                    'href': href,
                    'type': type_
                }
                
        return result
        
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Errore nel recupero del webfinger: {str(e)}")
    except json.JSONDecodeError:
        raise ValueError("Il documento webfinger non è in formato JSON valido")
    except Exception as e:
        raise Exception(f"Errore generico: {str(e)}")