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
    for schema in observer_schema:
        field = schema.get('field')
        if field not in last_applied_manifest:
            last_applied_manifest[field] = response.get(field, None)
        
        # If the schema has nested fields, we need to handle them recursively
        if 'nested' in schema:
            nested_schema = schema['nested']
            nested_response = response.get(field, {})
            if isinstance(last_applied_manifest[field], list):
                for item in last_applied_manifest[field]:
                    update_last_applied_manifest_list_from_resp(item, nested_schema, nested_response)
            else:
                update_last_applied_manifest_list_from_resp(last_applied_manifest[field], nested_schema, nested_response)

    return last_applied_manifest