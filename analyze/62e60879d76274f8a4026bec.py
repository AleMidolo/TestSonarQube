def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None,
          db=None, imp_user=None, dehydration_hooks=None,
          hydration_hooks=None, **handlers):
    # Inizializza la coda di output
    output_queue = []

    # Aggiungi il messaggio BEGIN alla coda
    begin_message = {
        "mode": mode or "WRITE",
        "bookmarks": bookmarks,
        "metadata": metadata,
        "timeout": timeout,
        "db": db,
        "imp_user": imp_user,
        "dehydration_hooks": dehydration_hooks,
        "hydration_hooks": hydration_hooks,
        "handlers": handlers
    }
    
    output_queue.append(begin_message)

    # Restituisci un oggetto Response
    return Response(output_queue)