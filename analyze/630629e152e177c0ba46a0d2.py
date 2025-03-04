def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Recupera e analizza un documento webfinger remoto di Diaspora.

    :arg handle: Handle remoto da recuperare  
    :returns: dict
    """
    import requests
    import json
    from urllib.parse import urlparse

    # Verifica formato handle
    if '@' not in handle:
        raise ValueError("Handle non valido - deve essere nel formato user@domain.tld")

    username, domain = handle.split('@')
    
    # Costruisci URL webfinger
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Recupera documento webfinger
        response = requests.get(webfinger_url, timeout=10)
        response.raise_for_status()
        
        # Analizza JSON
        webfinger_data = response.json()
        
        # Estrai informazioni rilevanti
        result = {
            'handle': handle,
            'username': username,
            'domain': domain,
            'links': {}
        }
        
        # Analizza i link nel documento webfinger
        if 'links' in webfinger_data:
            for link in webfinger_data['links']:
                if 'rel' in link:
                    result['links'][link['rel']] = {
                        'href': link.get('href', ''),
                        'type': link.get('type', '')
                    }
        
        return result
        
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Errore nel recupero del webfinger: {str(e)}")
    except json.JSONDecodeError:
        raise ValueError("Il documento webfinger non è in formato JSON valido")
    except Exception as e:
        raise Exception(f"Errore generico: {str(e)}")