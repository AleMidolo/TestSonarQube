def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None,
          db=None, imp_user=None, dehydration_hooks=None,
          hydration_hooks=None, **handlers):
    """
    Aggiunge un messaggio BEGIN alla coda di output.

    :param mode: modalità di accesso per il routing - "READ" o "WRITE" (predefinito)
    :param bookmarks: iterabile di valori di segnalibro dopo i quali questa transazione dovrebbe iniziare
    :param metadata: dizionario di metadati personalizzati da allegare alla transazione
    :param timeout: timeout per l'esecuzione della transazione (in secondi)
    :param db: nome del database su cui avviare la transazione
        Richiede Bolt 4.0+.
    :param imp_user: l'utente da impersonare
        Richiede Bolt 4.4+.
    :param dehydration_hooks:
        Hook per disidratare i tipi (dizionario da tipo (classe) a funzione di disidratazione).
        Le funzioni di disidratazione ricevono il valore e restituiscono un oggetto di tipo
        compreso da packstream.
    :param hydration_hooks:
        Hook per idratare i tipi (mappatura da tipo (classe) a funzione di idratazione).
        Le funzioni di idratazione ricevono il valore di tipo compreso da packstream
        e possono restituire qualsiasi cosa.
    :param handlers: funzioni gestore passate all'oggetto Response restituito
    :return: oggetto Response
    """
    # Inizializza il dizionario dei parametri extra
    extra = {}
    
    # Gestisce i bookmarks se presenti
    if bookmarks:
        extra["bookmarks"] = list(bookmarks)
        
    # Gestisce i metadata se presenti
    if metadata:
        extra["tx_metadata"] = metadata
        
    # Gestisce il timeout se presente
    if timeout:
        extra["tx_timeout"] = int(1000 * timeout)
        
    # Gestisce la modalità di accesso
    if mode:
        extra["mode"] = mode
        
    # Gestisce il database target se presente
    if db:
        extra["db"] = db
        
    # Gestisce l'impersonazione utente se presente
    if imp_user:
        extra["imp_user"] = imp_user

    # Crea il messaggio BEGIN
    message = {
        "type": "BEGIN",
        "extra": extra
    }
    
    # Configura gli hook di serializzazione/deserializzazione
    if dehydration_hooks:
        message["dehydration_hooks"] = dehydration_hooks
    if hydration_hooks:
        message["hydration_hooks"] = hydration_hooks

    # Aggiunge il messaggio alla coda di output
    self._append(message, Response(**handlers))
    
    # Restituisce l'oggetto Response
    return self._responses[-1]