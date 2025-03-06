def verify_relayable_signature(public_key, doc, signature):
    """
    Verifica gli elementi XML firmati per avere la certezza che l'autore dichiarato abbia effettivamente generato questo messaggio.
    
    :param public_key: La chiave pubblica utilizzata per verificare la firma.
    :param doc: Il documento XML firmato.
    :param signature: La firma da verificare.
    :return: True se la firma è valida, False altrimenti.
    """
    from Crypto.PublicKey import RSA
    from Crypto.Signature import pkcs1_15
    from Crypto.Hash import SHA256
    from lxml import etree

    # Estrai il contenuto firmato dal documento XML
    root = etree.fromstring(doc)
    signed_content = etree.tostring(root, method="c14n")

    # Crea un oggetto hash del contenuto firmato
    hash_obj = SHA256.new(signed_content)

    # Verifica la firma
    try:
        rsa_key = RSA.import_key(public_key)
        pkcs1_15.new(rsa_key).verify(hash_obj, signature)
        return True
    except (ValueError, TypeError):
        return False