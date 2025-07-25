import json

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Generate a NodeInfo .well-known document.

    See spec: http://nodeinfo.diaspora.software

    :arg url: The full base url with protocol, ie https://example.com
    :arg document_path: Custom NodeInfo document path if supplied (optional)
    :returns: dict
    """
    if document_path is None:
        document_path = "/.well-known/nodeinfo"
    
    well_known_url = f"{url.rstrip('/')}{document_path}"
    
    document = {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": f"{url.rstrip('/')}/nodeinfo/2.0"
            },
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.1",
                "href": f"{url.rstrip('/')}/nodeinfo/2.1"
            }
        ]
    }
    
    return document