def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    """
    Asegúrate de que los identificadores del remitente y de la entidad coincidan.

    Básicamente, ya hemos verificado que el remitente es quien dice ser al recibir la carga útil (payload). Sin embargo, el remitente podría estar intentando establecer otro autor en la propia carga útil, ya que Diaspora incluye al remitente tanto en los encabezados de la carga útil como en el objeto. Debemos asegurarnos de que sean iguales.
    """
    return sender_handle == entity_handle