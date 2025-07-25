from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def verify_relayable_signature(public_key, doc, signature):
    """
    हस्ताक्षरित XML तत्वों को सत्यापित करें ताकि यह सुनिश्चित किया जा सके 
    कि दावा किया गया लेखक ने वास्तव में यह संदेश उत्पन्न किया है।
    
    :param public_key: सार्वजनिक कुंजी (PEM प्रारूप में)
    :param doc: सत्यापित करने के लिए दस्तावेज़ (बाइट्स में)
    :param signature: हस्ताक्षर (बाइट्स में)
    :return: बूलियन, यदि हस्ताक्षर सत्यापित होता है तो True, अन्यथा False
    """
    try:
        # सार्वजनिक कुंजी को लोड करें
        pub_key = serialization.load_pem_public_key(
            public_key,
            backend=default_backend()
        )
        
        # हस्ताक्षर को सत्यापित करें
        pub_key.verify(
            signature,
            doc,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        # यदि सत्यापन विफल होता है, तो False लौटाएं
        return False