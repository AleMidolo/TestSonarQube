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
    # Default document path if none provided
    if document_path is None:
        document_path = "/nodeinfo/2.0"

    # Remove trailing slash from URL if present
    if url.endswith('/'):
        url = url[:-1]

    # Create the well-known document
    well_known = {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": f"{url}{document_path}"
            }
        ]
    }

    return well_known