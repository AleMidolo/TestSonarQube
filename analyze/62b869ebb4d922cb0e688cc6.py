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
    for schema_field in observer_schema:
        if isinstance(schema_field, dict):
            field_name = schema_field.get('name')
            if field_name not in last_applied_manifest:
                last_applied_manifest[field_name] = response.get(field_name, None)
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[field_name], 
                schema_field.get('children', []), 
                response.get(field_name, {})
            )
        elif isinstance(schema_field, str):
            if schema_field not in last_applied_manifest:
                last_applied_manifest[schema_field] = response.get(schema_field, None)
    return last_applied_manifest