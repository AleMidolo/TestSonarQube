def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    Junto con :func:``update_last_applied_manifest_list_from_resp``, esta
    función se llama de forma recursiva para actualizar un ``last_applied_manifest``
    parcial a partir de una respuesta parcial de Kubernetes.

    Argumentos:
        last_applied_manifest (dict): ``last_applied_manifest`` parcial que se está
            actualizando.
        observer_schema (dict): ``observer_schema`` parcial.
        response (dict): respuesta parcial de la API de Kubernetes.

    Excepciones:
        KeyError: Si el campo observado no está presente en la respuesta de Kubernetes.

    Esta función recorre todos los campos observados e inicializa su valor en
    ``last_applied_manifest`` si aún no están presentes.
    """
    for key, schema in observer_schema.items():
        if key not in response:
            raise KeyError(f"Field '{key}' not found in Kubernetes response.")
        
        if isinstance(schema, dict):
            if key not in last_applied_manifest:
                last_applied_manifest[key] = {}
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[key], schema, response[key]
            )
        elif isinstance(schema, list):
            if key not in last_applied_manifest:
                last_applied_manifest[key] = []
            # Assuming there's a function `update_last_applied_manifest_list_from_resp`
            # to handle list types.
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[key], schema, response[key]
            )
        else:
            if key not in last_applied_manifest:
                last_applied_manifest[key] = response[key]