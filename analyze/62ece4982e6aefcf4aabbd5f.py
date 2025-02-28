def paging(response, max_results):
    """
    WAPI प्रतिक्रिया को पेज दर पेज लौटाता है।

    आर्ग्युमेंट्स:
        response (list): WAPI प्रतिक्रिया।
        max_results (int): एक पेज में लौटाए जाने वाले ऑब्जेक्ट्स की अधिकतम संख्या।
    
    रिटर्न्स:
        Generator object: WAPI प्रतिक्रिया को पेज दर पेज विभाजित करके लौटाता है।
    """
    for i in range(0, len(response), max_results):
        yield response[i:i + max_results]