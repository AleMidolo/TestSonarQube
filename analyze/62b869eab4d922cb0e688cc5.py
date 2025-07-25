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
    """
    # Go through all fields in the observer schema
    for field, schema in observer_schema.items():
        # Skip if field is already in last_applied_manifest
        if field in last_applied_manifest:
            continue
            
        # Get value from response, raise KeyError if not found
        try:
            value = response[field]
        except KeyError:
            raise KeyError(f"Field {field} not found in Kubernetes response")
            
        # Handle nested dictionaries recursively
        if isinstance(schema, dict) and isinstance(value, dict):
            last_applied_manifest[field] = {}
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[field], schema, value
            )
            
        # Handle lists recursively if schema is a dict
        elif isinstance(schema, dict) and isinstance(value, list):
            last_applied_manifest[field] = []
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[field], schema, value
            )
            
        # For simple values, just copy them over
        else:
            last_applied_manifest[field] = value