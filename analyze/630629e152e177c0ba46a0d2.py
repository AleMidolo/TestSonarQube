def retrieve_and_parse_diaspora_webfinger(handle):
    """
    डायस्पोरा वेबफिंगर डॉक्यूमेंट को प्राप्त करें और पार्स करें।

    :पैरामीटर हैंडल: प्राप्त करने के लिए रिमोट हैंडल  
    :वापसी: डिक्शनरी (dict)
    """
    import requests
    import json

    # Construct the webfinger URL
    webfinger_url = f"https://{handle}/.well-known/webfinger?resource=acct:{handle}"

    # Make a GET request to retrieve the webfinger document
    response = requests.get(webfinger_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        webfinger_data = response.json()
        return webfinger_data
    else:
        # Handle errors (e.g., user not found, server error)
        return {"error": "Unable to retrieve webfinger document", "status_code": response.status_code}