def _update_context(self, context):
    """
    Aggiorna il *context* con le proprietà di questo grafo.

    *context.error* viene aggiornato aggiungendo gli indici degli errori.
    Esempio di subcontext per un grafo con i campi "E,t,error_E_low":
    `{"error": {"x_low": {"index": 2}}}`.
    Nota che i nomi degli errori sono chiamati "x", "y" e "z"
    (questo corrisponde alle prime tre coordinate, se presenti),
    il che consente di semplificare la rappresentazione grafica.
    I valori esistenti non vengono rimossi
    da *context.value* e dai suoi subcontesti.

    Viene chiamato durante la "distruzione" del grafo (ad esempio,
    nella classe :class:`.ToCSV`). Per "distruzione" si intende la conversione
    in un'altra struttura (come il testo) nel flusso di lavoro.
    L'oggetto grafo non viene realmente distrutto in questo processo.
    """
    # Supponiamo che self.graph contenga le informazioni del grafo
    # e che context sia un dizionario con le chiavi 'error' e 'value'
    
    if 'error' not in context:
        context['error'] = {}
    
    # Aggiorna gli errori nel contesto
    for index, error in enumerate(self.graph.errors):
        error_key = f"x" if index == 0 else f"y" if index == 1 else f"z"
        context['error'][f"{error_key}_low"] = {'index': error.index}
    
    # Non rimuoviamo i valori esistenti in context.value
    # Preserviamo context.value e i suoi subcontesti