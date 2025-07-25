from typing import Optional
import requests

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    एक RFC7033 वेबफिंगर दस्तावेज़ प्राप्त करने का प्रयास करें। 
    यदि यह विफल होता है, तो कोई अपवाद उत्पन्न नहीं करता।
    """
    try:
        response = requests.get(f"https://webfinger.example.com/well-known/webfinger?resource=acct:{handle}")
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return None