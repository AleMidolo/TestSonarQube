def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Generate a NodeInfo .well-known document.

    See spec: http://nodeinfo.diaspora.software

    :arg url: The full base url with protocol, ie https://example.com
    :arg document_path: Custom NodeInfo document path if supplied (optional)
    :returns: dict
    """
    if not document_path:
        document_path = "/nodeinfo/2.0"

    # Remove trailing slash from url if present
    if url.endswith("/"):
        url = url[:-1]
        
    return {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": f"{url}{document_path}"
            }
        ]
    }