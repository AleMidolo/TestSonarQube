def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    Insieme alla funzione :func:``update_last_applied_manifest_list_from_resp``, 
    questa funzione viene chiamata ricorsivamente per aggiornare un 
    ``last_applied_manifest`` parziale a partire da una risposta parziale di Kubernetes.

    Argomenti:
        last_applied_manifest (dict): ``last_applied_manifest`` parziale in fase di aggiornamento
        observer_schema (dict): ``observer_schema`` parziale
        response (dict): risposta parziale dall'API di Kubernetes.

    Eccezioni:
        KeyError: Se il campo osservato non è presente nella risposta di Kubernetes.

    Questa funzione analizza tutti i campi osservati e inizializza il loro valore 
    in ``last_applied_manifest`` se non sono ancora presenti.
    """
    for key, value in observer_schema.items():
        if isinstance(value, dict):
            # Recursive call for nested dictionaries
            if key not in last_applied_manifest:
                last_applied_manifest[key] = {}
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[key], value, response.get(key, {})
            )
        else:
            # Check if the key is in the response and update last_applied_manifest
            if key not in last_applied_manifest:
                if key not in response:
                    raise KeyError(f"Field '{key}' is not present in the Kubernetes response.")
                last_applied_manifest[key] = response[key]