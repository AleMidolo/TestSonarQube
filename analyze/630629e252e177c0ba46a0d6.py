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

    # Effettuare la richiesta GET
    response = requests.get(url)

    # Verificare se la richiesta ha avuto successo
    if response.status_code == 200:
        # Analizzare il contenuto XML
        xrd = etree.fromstring(response.content)
        return xrd
    else:
        response.raise_for_status()