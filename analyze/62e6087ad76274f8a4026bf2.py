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
    # Crear el mensaje DISCARD
    discard_message = {
        "type": "DISCARD",
        "n": n,
        "qid": qid
    }

    # Aplicar los ganchos de deshidratación si están presentes
    if dehydration_hooks:
        discard_message["dehydration_hooks"] = dehydration_hooks

    # Aplicar los ganchos de hidratación si están presentes
    if hydration_hooks:
        discard_message["hydration_hooks"] = hydration_hooks

    # Añadir los manejadores adicionales
    discard_message.update(handlers)

    # Añadir el mensaje a la cola de salida
    self.output_queue.append(discard_message)

    # Devolver el objeto Response con los manejadores
    return Response(handlers=handlers)