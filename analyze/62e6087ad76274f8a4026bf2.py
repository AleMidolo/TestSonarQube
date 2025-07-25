def discard(self, n=-1, qid=-1, dehydration_hooks=None,
            hydration_hooks=None, **handlers):
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
    # Implementación del método
    message = {
        'type': 'DISCARD',
        'n': n,
        'qid': qid,
        'dehydration_hooks': dehydration_hooks,
        'hydration_hooks': hydration_hooks,
        'handlers': handlers
    }
    
    # Aquí se añadiría el mensaje a la cola de salida
    self.output_queue.append(message)