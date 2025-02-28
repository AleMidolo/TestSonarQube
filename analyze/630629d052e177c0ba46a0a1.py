import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.

    :param public_key: The public key used for verification.
    :param doc: The XML document to verify.
    :param signature: The signature to verify against the document.
    :return: True if the signature is valid, False otherwise.
    """
    try:
        # Load the public key
        pub_key = serialization.load_pem_public_key(public_key)

        # Parse the XML document
        root = ET.fromstring(doc)

        # Extract the signed elements
        signed_elements = root.findall(".//*[@signed='true']")

        # Concatenate the signed elements
        signed_data = ''.join([ET.tostring(element, encoding='unicode') for element in signed_elements])

        # Verify the signature
        pub_key.verify(
            signature,
            signed_data.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False