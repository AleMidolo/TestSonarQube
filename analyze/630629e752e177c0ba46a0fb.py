import requests

def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    """
    यह एक सहायक मेथड है जो POST के माध्यम से एक दस्तावेज़ (डॉक्यूमेंट) भेजने के लिए उपयोग किया जाता है।

    अतिरिक्त ``*args`` और ``**kwargs`` को ``requests.post`` में पास किया जाएगा।

    पैरामीटर (Arguments):
    - url: वह पूर्ण URL (प्रोटोकॉल सहित) जहां डेटा भेजा जाना है।
    - data: एक डिक्शनरी (जो फॉर्म-एन्कोडेड होगी), बाइट्स, या फाइल-जैसे ऑब्जेक्ट जिसे बॉडी में भेजा जाएगा।
    - timeout: प्रतिक्रिया (response) के लिए प्रतीक्षा करने का समय, सेकंड में (डिफ़ॉल्ट रूप से 10 सेकंड)।
    - method: उपयोग की जाने वाली HTTP विधि, डिफ़ॉल्ट रूप से "post"।

    रिटर्न (Returns):
    - status code: एक ट्यूपल जिसमें HTTP स्थिति कोड (int या None) होता है।
    - error: एक अपवाद (exception) क्लास का उदाहरण या None।
    """
    try:
        if method.lower() == "post":
            response = requests.post(url, data=data, timeout=timeout, *args, **kwargs)
        else:
            raise ValueError("Unsupported HTTP method. Only 'post' is supported.")
        
        return response.status_code, None
    except Exception as e:
        return None, e