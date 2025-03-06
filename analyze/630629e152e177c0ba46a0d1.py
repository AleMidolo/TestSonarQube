import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Prova a recuperare un documento webfinger conforme a RFC7033. Non genera eccezioni in caso di fallimento.
    """
    try:
        # Estrai il dominio dall'handle
        domain = handle.split('@')[-1]
        webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
        
        # Effettua la richiesta HTTP
        response = requests.get(webfinger_url, timeout=5)
        response.raise_for_status()  # Solleva un'eccezione per codici di stato HTTP non validi
        
        # Restituisci il contenuto del documento webfinger
        return response.text
    except (requests.RequestException, IndexError):
        # In caso di errore, restituisci None
        return None