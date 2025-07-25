def discard(self, n=-1, qid=-1, dehydration_hooks=None, hydration_hooks=None, **handlers):
    """
    Aggiunge un messaggio DISCARD alla coda di output.

    :param n: numero di record da scartare, valore predefinito = -1 (TUTTI)
    :param qid: ID della query per cui scartare, valore predefinito = -1 (ultima query)
    :param dehydration_hooks:
        Hook per disidratare i tipi (dizionario da tipo (classe) a funzione di disidratazione).
        Le funzioni di disidratazione ricevono il valore e restituiscono un oggetto di tipo
        comprensibile da packstream.
    :param hydration_hooks:
        Hook per idratare i tipi (mappatura da tipo (classe) a funzione di idratazione).
        Le funzioni di idratazione ricevono il valore di un tipo comprensibile da packstream
        e possono restituire qualsiasi cosa.
    :param handlers: funzioni gestore passate all'oggetto Response restituito
    """
    # Creazione del messaggio DISCARD
    discard_message = {
        "type": "DISCARD",
        "n": n,
        "qid": qid
    }

    # Aggiunta degli hook di disidratazione e idratazione se forniti
    if dehydration_hooks is not None:
        discard_message["dehydration_hooks"] = dehydration_hooks
    if hydration_hooks is not None:
        discard_message["hydration_hooks"] = hydration_hooks

    # Aggiunta degli handler se forniti
    if handlers:
        discard_message.update(handlers)

    # Aggiunta del messaggio alla coda di output
    self.output_queue.append(discard_message)

    # Restituzione dell'oggetto Response
    return Response(discard_message)