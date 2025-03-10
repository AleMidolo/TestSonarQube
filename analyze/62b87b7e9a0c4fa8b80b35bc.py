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

    # Aggiorna gli errori con gli indici corrispondenti
    for i, field in enumerate(self.fields):
        if field.startswith('error_'):
            error_type = field.split('_')[1]
            error_name = field.split('_')[2]
            if error_type not in context.error:
                context.error[error_type] = {}
            context.error[error_type][error_name] = {'index': i}

    # Mantieni i valori esistenti in context.value
    if not hasattr(context, 'value'):
        context.value = {}
    for key, value in self.values.items():
        if key not in context.value:
            context.value[key] = value