def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    Insieme alla funzione :func:``update_last_applied_manifest_dict_from_resp``, 
    questa funzione viene chiamata ricorsivamente per aggiornare un 
    ``last_applied_manifest`` parziale a partire da una risposta parziale di Kubernetes.

    Argomenti:
        last_applied_manifest (list): ``last_applied_manifest`` parziale in fase di aggiornamento.
        observer_schema (list): ``observer_schema`` parziale.
        response (list): risposta parziale dall'API di Kubernetes.

    Questa funzione attraversa tutti i campi osservati e inizializza il loro valore 
    in ``last_applied_manifest`` se non sono ancora presenti.
    """
    for schema in observer_schema:
        field = schema.get('field')
        if field not in last_applied_manifest:
            for resp in response:
                if field in resp:
                    last_applied_manifest[field] = resp[field]
                    break
    return last_applied_manifest