import requests

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    डायस्पोरा वेबफिंगर डॉक्यूमेंट को प्राप्त करें और पार्स करें।

    :पैरामीटर हैंडल: प्राप्त करने के लिए रिमोट हैंडल  
    :वापसी: डिक्शनरी (dict)
    """
    url = f"https://{handle}/.well-known/webfinger?resource=acct:{handle}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()