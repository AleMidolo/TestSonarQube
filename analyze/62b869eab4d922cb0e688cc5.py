def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    Together with :func:``update_last_applied_manifest_list_from_resp``, this
    function is called recursively to update a partial ``last_applied_manifest``
    from a partial Kubernetes response

    Args:
        last_applied_manifest (dict): partial ``last_applied_manifest`` being
            updated
        observer_schema (dict): partial ``observer_schema``
        response (dict): partial response from the Kubernetes API.

    Raises:
        KeyError: If the observed field is not present in the Kubernetes response

    This function go through all observed fields, and initialized their value in
    last_applied_manifest if they are not yet present
    """
    for field, schema in observer_schema.items():
        if field not in response:
            raise KeyError(f"Field '{field}' not found in the Kubernetes response.")
        
        if field not in last_applied_manifest:
            if isinstance(schema, dict):
                last_applied_manifest[field] = {}
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest[field], schema, response[field]
                )
            elif isinstance(schema, list):
                last_applied_manifest[field] = []
                update_last_applied_manifest_list_from_resp(
                    last_applied_manifest[field], schema, response[field]
                )
            else:
                last_applied_manifest[field] = response[field]
        else:
            if isinstance(schema, dict):
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest[field], schema, response[field]
                )
            elif isinstance(schema, list):
                update_last_applied_manifest_list_from_resp(
                    last_applied_manifest[field], schema, response[field]
                )
            else:
                last_applied_manifest[field] = response[field]