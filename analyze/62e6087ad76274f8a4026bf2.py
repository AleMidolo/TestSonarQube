def discard(self, n=-1, qid=-1, dehydration_hooks=None, hydration_hooks=None, **handlers):
    """
    Añade un mensaje 'DISCARD' a la cola de salida.

    :param n: número de registros a descartar, por defecto = -1 (TODOS)
    :param qid: ID de consulta para descartar, por defecto = -1 (última consulta)
    :param dehydration_hooks:
        Ganchos para deshidratar tipos (diccionario de tipo (clase) a función
        de deshidratación). Las funciones de deshidratación reciben el valor y devuelven un objeto de un tipo entendido por 'packstream'.
    :param hydration_hooks:
        Ganchos para hidratar tipos (mapeo de tipo (clase) a función de
     hidratación). Las funciones de hidratación reciben el valor de un tipo
        entendido por 'packstream' y son libres de devolver cualquier cosa.
    :param handlers: funciones manejadoras pasadas al objeto 'Response' devuelto
    """
    if qid == -1:
        qid = self._last_qid
        
    # Crear mensaje DISCARD
    message = {
        "type": "DISCARD",
        "n": n,
        "qid": qid
    }
    
    # Aplicar hooks de deshidratación si existen
    if dehydration_hooks:
        for type_, hook in dehydration_hooks.items():
            if isinstance(message, type_):
                message = hook(message)
                
    # Añadir mensaje a la cola de salida
    self._outbound_messages.append(message)
    
    # Crear y devolver objeto Response con los handlers proporcionados
    response = Response(
        connection=self,
        hydration_hooks=hydration_hooks or {},
        **handlers
    )
    
    return response