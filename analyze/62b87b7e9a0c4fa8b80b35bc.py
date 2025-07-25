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
    for i, error_key in enumerate(['x', 'y', 'z']):
        if hasattr(self, f'error_{error_key}_low'):
            context.error[f'{error_key}_low'] = {'index': i * 2}
        if hasattr(self, f'error_{error_key}_high'):
            context.error[f'{error_key}_high'] = {'index': i * 2 + 1}

    # Mantieni i valori esistenti in context.value
    if not hasattr(context, 'value'):
        context.value = {}

    # Aggiungi eventuali altre proprietà del grafo al contesto
    for key, value in self.__dict__.items():
        if key not in ['error_x_low', 'error_x_high', 'error_y_low', 'error_y_high', 'error_z_low', 'error_z_high']:
            context.value[key] = value