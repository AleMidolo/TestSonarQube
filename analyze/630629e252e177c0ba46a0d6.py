def retrieve_diaspora_host_meta(host):
    """
    Recupera un documento host-meta remoto di Diaspora.

    :arg host: Host da cui recuperare
    :returns: Istanza di ``XRD``
    """
    import requests
    from lxml import etree

    # Costruire l'URL del documento host-meta
    url = f"https://{host}/host-meta"

    try:
        # Effettuare la richiesta GET
        response = requests.get(url)
        response.raise_for_status()  # Solleva un'eccezione per risposte di errore

        # Analizzare il contenuto XML
        xrd = etree.fromstring(response.content)

        return xrd  # Restituisce l'istanza di XRD

    except requests.RequestException as e:
        print(f"Errore durante il recupero del documento host-meta: {e}")
        return None