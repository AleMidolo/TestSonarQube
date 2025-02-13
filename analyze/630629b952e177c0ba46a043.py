def get_nodeinfo_well_known_document(url, document_path=None):
    nodeinfo = {
        "version": "2.0",
        "links": [
            {
                "rel": "self",
                "href": f"{url}/{document_path or 'nodeinfo'}"
            },
            {
                "rel": "http://webfinger.net/rel/profile-page",
                "href": url
            },
            {
                "rel": "http://webfinger.net/rel/registration",
                "href": f"{url}/register"
            }
        ]
    }
    return nodeinfo