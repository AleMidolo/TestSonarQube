def base_config(user, etcd_host="localhost", etcd_port=2379):
    """
    यह फ़ंक्शन कुछ सरल पैरामीटरों के साथ एक कॉन्फ़िगरेशन बनाता है, जिनके लिए डिफ़ॉल्ट मान सेट किया जा सकता है।  

    पैरामीटर (Args):
    - user (str): स्थिर प्रमाणीकरण (static authentication) के लिए उपयोगकर्ता का नाम।  
    - etcd_host (str): डेटाबेस के लिए होस्ट।  
    - etcd_port (int): डेटाबेस के लिए पोर्ट। 

    रिटर्न (Returns):
    - dict: बनाया गया कॉन्फ़िगरेशन।  
    """
    config = {
        "user": user,
        "database": {
            "host": etcd_host,
            "port": etcd_port
        },
        "version": "1.0"
    }
    
    return config