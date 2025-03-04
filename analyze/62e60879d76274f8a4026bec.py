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
    
    # Aggiungi i bookmarks se specificati
    if bookmarks:
        extra["bookmarks"] = list(bookmarks)
        
    # Aggiungi i metadata se specificati
    if metadata:
        extra["tx_metadata"] = metadata
        
    # Aggiungi il timeout se specificato
    if timeout:
        extra["tx_timeout"] = timeout
        
    # Aggiungi il database se specificato
    if db:
        extra["db"] = db
        
    # Aggiungi l'utente da impersonare se specificato
    if imp_user:
        extra["imp_user"] = imp_user

    # Aggiungi la modalità se specificata, altrimenti usa "WRITE" come default
    if mode:
        extra["mode"] = mode
    else:
        extra["mode"] = "WRITE"

    # Configura gli hook di serializzazione se specificati
    if dehydration_hooks:
        self.dehydration_hooks.update(dehydration_hooks)
    if hydration_hooks:
        self.hydration_hooks.update(hydration_hooks)

    # Crea e restituisce un nuovo oggetto Response con i parametri specificati
    return Response(self, "BEGIN", extra, **handlers)