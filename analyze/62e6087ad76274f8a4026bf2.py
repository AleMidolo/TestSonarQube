def discard(self, n=-1, qid=-1, dehydration_hooks=None,
            hydration_hooks=None, **handlers):
    """
    Appends a DISCARD message to the output queue.

    :param n: number of records to discard, default = -1 (ALL)
    :param qid: query ID to discard for, default = -1 (last query)
    :param dehydration_hooks:
        Hooks to dehydrate types (dict from type (class) to dehydration
        function). Dehydration functions receive the value and returns an
        object of type understood by packstream.
    :param hydration_hooks:
        Hooks to hydrate types (mapping from type (class) to
        dehydration function). Dehydration functions receive the value of
        type understood by packstream and are free to return anything.
    :param handlers: handler functions passed into the returned Response object
    """
    # Create the DISCARD message
    discard_message = {
        "type": "DISCARD",
        "n": n,
        "qid": qid,
        "dehydration_hooks": dehydration_hooks or {},
        "hydration_hooks": hydration_hooks or {},
        **handlers
    }
    
    # Append the message to the output queue
    self.output_queue.append(discard_message)
    
    # Return a Response object with the handlers
    return Response(handlers=handlers)