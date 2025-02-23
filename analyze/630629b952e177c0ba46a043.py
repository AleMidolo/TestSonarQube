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
    nodeinfo = {
        "version": "2.0",
        "links": [
            {
                "rel": "self",
                "href": f"{url}/{document_path or '.well-known/nodeinfo'}"
            }
        ]
    }
    return nodeinfo