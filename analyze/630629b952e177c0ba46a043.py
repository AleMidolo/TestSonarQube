def get_nodeinfo_well_known_document(url, document_path=None):
    """
    NodeInfo .well-known दस्तावेज़ उत्पन्न करें।  

    स्पेसिफिकेशन देखें: [http://nodeinfo.diaspora.software](http://nodeinfo.diaspora.software)  

    पैरामीटर (Arguments): 
    - url: पूरा बेस URL प्रोटोकॉल के साथ, जैसे `https://example.com`  
    - document_path: कस्टम NodeInfo दस्तावेज़ पथ, यदि प्रदान किया गया हो (वैकल्पिक)  

    रिटर्न (Returns):  
    - dict: एक स्वरूपित डिक्शनरी
    """
    import json

    nodeinfo_document = {
        "version": "2.0",
        "software": {
            "name": "YourSoftwareName",
            "version": "1.0.0"
        },
        "protocols": [
            "activitypub",
            "activitystreams",
            "webfinger"
        ],
        "services": {
            "outbound": [
                {
                    "name": "Service Name",
                    "url": "https://service.example.com"
                }
            ],
            "inbound": [
                {
                    "name": "Another Service",
                    "url": "https://another.service.example.com"
                }
            ]
        },
        "metadata": {
            "description": "A brief description of the node.",
            "icon": {
                "type": "image/png",
                "url": f"{url}/path/to/icon.png"
            }
        }
    }

    if document_path:
        nodeinfo_url = f"{url}/{document_path}"
    else:
        nodeinfo_url = f"{url}/.well-known/nodeinfo"

    return {
        "nodeinfo": nodeinfo_url,
        "data": nodeinfo_document
    }