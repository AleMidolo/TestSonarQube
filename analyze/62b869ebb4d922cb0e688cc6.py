def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    Together with :func:``update_last_applied_manifest_dict_from_resp``, this
    function is called recursively to update a partial ``last_applied_manifest``
    from a partial Kubernetes response

    Args:
        last_applied_manifest (list): partial ``last_applied_manifest`` being
            updated
        observer_schema (list): partial ``observer_schema``
        response (list): partial response from the Kubernetes API.

    This function go through all observed fields, and initialized their value in
    last_applied_manifest if they are not yet present
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