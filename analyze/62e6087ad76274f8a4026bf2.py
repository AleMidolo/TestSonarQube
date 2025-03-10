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
        "qid": qid,
        "dehydration_hooks": dehydration_hooks if dehydration_hooks else {},
        "hydration_hooks": hydration_hooks if hydration_hooks else {},
        **handlers
    }
    
    # Aggiunta del messaggio alla coda di output
    self.output_queue.append(discard_message)
    
    # Restituzione dell'oggetto Response con i gestori
    return Response(handlers=handlers)