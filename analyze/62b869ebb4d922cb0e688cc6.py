def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    Junto con :func:``update_last_applied_manifest_dict_from_resp``, esta
    función se llama de forma recursiva para actualizar un ``last_applied_manifest``
    parcial a partir de una respuesta parcial de Kubernetes.

    Argumentos:
        last_applied_manifest (list): ``last_applied_manifest`` parcial que se
            está actualizando.
        observer_schema (list): ``observer_schema`` parcial.
        response (list): respuesta parcial de la API de Kubernetes.

    Esta función recorre todos los campos observados e inicializa su valor en
    ``last_applied_manifest`` si aún no están presentes.
    """
    for i, (schema_item, resp_item) in enumerate(zip(observer_schema, response)):
        if isinstance(schema_item, dict) and isinstance(resp_item, dict):
            if i >= len(last_applied_manifest):
                last_applied_manifest.append({})
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
        elif isinstance(schema_item, list) and isinstance(resp_item, list):
            if i >= len(last_applied_manifest):
                last_applied_manifest.append([])
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
        else:
            if i >= len(last_applied_manifest):
                last_applied_manifest.append(resp_item)
            else:
                last_applied_manifest[i] = resp_item