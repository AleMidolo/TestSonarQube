import requests

def retrieve_and_parse_diaspora_webfinger(handle):
    url = f"https://{handle}/.well-known/webfinger?resource=acct:{handle}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()