def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    """
    Assicurati che i valori di `sender_handle` e `entity_handle` corrispondano.

    Fondamentalmente, abbiamo già verificato che il mittente sia chi dichiara di essere al momento della ricezione del payload. Tuttavia, il mittente potrebbe cercare di impostare un altro autore all'interno del payload stesso, poiché 'Diaspora' include il mittente sia negli header del payload che nell'oggetto. Dobbiamo garantire che siano identici.
    """
    return sender_handle == entity_handle