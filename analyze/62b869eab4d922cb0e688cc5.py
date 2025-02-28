def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    Aggiorna un last_applied_manifest parziale a partire da una risposta parziale di Kubernetes.

    Args:
        last_applied_manifest (dict): last_applied_manifest parziale in fase di aggiornamento.
        observer_schema (dict): observer_schema parziale.
        response (dict): risposta parziale dall'API di Kubernetes.

    Raises:
        KeyError: Se il campo osservato non è presente nella risposta di Kubernetes.
    """
    for key, schema in observer_schema.items():
        if key not in response:
            raise KeyError(f"Campo osservato '{key}' non presente nella risposta di Kubernetes.")
        
        if isinstance(schema, dict):
            if key not in last_applied_manifest:
                last_applied_manifest[key] = {}
            update_last_applied_manifest_dict_from_resp(last_applied_manifest[key], schema, response[key])
        elif isinstance(schema, list):
            if key not in last_applied_manifest:
                last_applied_manifest[key] = []
            update_last_applied_manifest_list_from_resp(last_applied_manifest[key], schema, response[key])
        else:
            if key not in last_applied_manifest:
                last_applied_manifest[key] = response[key]

def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    Aggiorna un last_applied_manifest parziale (lista) a partire da una risposta parziale di Kubernetes.

    Args:
        last_applied_manifest (list): last_applied_manifest parziale in fase di aggiornamento.
        observer_schema (list): observer_schema parziale.
        response (list): risposta parziale dall'API di Kubernetes.

    Raises:
        KeyError: Se il campo osservato non è presente nella risposta di Kubernetes.
    """
    for i, item in enumerate(response):
        if i >= len(last_applied_manifest):
            last_applied_manifest.append({})
        if isinstance(observer_schema[0], dict):
            update_last_applied_manifest_dict_from_resp(last_applied_manifest[i], observer_schema[0], item)
        else:
            last_applied_manifest[i] = item