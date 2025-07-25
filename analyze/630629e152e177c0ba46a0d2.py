def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Recupera y analiza un documento "webfinger" remoto de Diaspora.

    :arg handle: Identificador remoto a recuperar 
    :returns: dict
    """
    import requests
    import json
    from urllib.parse import urlparse

    # Validar formato del handle
    if '@' not in handle:
        raise ValueError("Handle debe tener formato usuario@dominio")
        
    # Separar usuario y dominio
    username, domain = handle.split('@')
    
    # Construir URL webfinger
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Hacer petición HTTP
        response = requests.get(webfinger_url, timeout=10)
        response.raise_for_status()
        
        # Parsear respuesta JSON
        data = response.json()
        
        # Validar formato de respuesta
        if 'subject' not in data or not data.get('links'):
            raise ValueError("Formato de respuesta webfinger inválido")
            
        # Construir diccionario de respuesta
        result = {
            'subject': data['subject'],
            'aliases': data.get('aliases', []),
            'links': {}
        }
        
        # Procesar links
        for link in data['links']:
            if 'rel' in link and 'href' in link:
                result['links'][link['rel']] = link['href']
                
        return result
        
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Error al recuperar webfinger: {str(e)}")
    except json.JSONDecodeError:
        raise ValueError("Respuesta webfinger no es JSON válido")