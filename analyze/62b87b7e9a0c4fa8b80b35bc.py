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
    if not hasattr(context, 'error'):
        context.error = {}

    # Aggiorna il contesto con gli indici degli errori
    for i, field in enumerate(self.fields):
        if field.startswith('error_'):
            error_type = field.split('_')[1]
            axis = 'x' if i % 3 == 0 else 'y' if i % 3 == 1 else 'z'
            error_key = f"{axis}_{error_type}"
            context.error[error_key] = {"index": i}

    # Mantieni i valori esistenti nel contesto
    if not hasattr(context, 'value'):
        context.value = {}
    # Non rimuovere i valori esistenti
    # (il contesto.value e i suoi subcontesti rimangono invariati)