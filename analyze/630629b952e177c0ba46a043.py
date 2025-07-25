def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Generate a NodeInfo .well-known document.

    See spec: http://nodeinfo.diaspora.software

    :arg url: The full base url with protocol, ie https://example.com
    :arg document_path: Custom NodeInfo document path if supplied (optional)
    :returns: dict
    """
    import json

    nodeinfo_document = {
        "version": "2.0",
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": f"{url}/{document_path or 'nodeinfo'}"
            }
        ]
    }

    return nodeinfo_document