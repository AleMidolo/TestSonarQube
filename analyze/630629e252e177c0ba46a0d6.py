def retrieve_diaspora_host_meta(host):
    """
    Recupera un documento host-meta remoto di Diaspora.

    :arg host: Host da cui recuperare
    :returns: Istanza di ``XRD``
    """
    import requests
    from lxml import etree

    # Costruire l'URL del documento host-meta
    host_meta_url = f"https://{host}/host-meta"

    # Effettuare la richiesta GET per recuperare il documento
    response = requests.get(host_meta_url)

    # Verificare se la richiesta ha avuto successo
    if response.status_code == 200:
        # Analizzare il documento XML
        xrd = etree.fromstring(response.content)
        return xrd
    else:
        response.raise_for_status()