def update_last_applied_manifest_dict_from_resp(last_applied_manifest, observer_schema, response):
    """
    Updates the partial `last_applied_manifest` from a partial Kubernetes response recursively.

    Args:
        last_applied_manifest (dict): The partial `last_applied_manifest` being updated.
        observer_schema (dict): The partial `observer_schema`.
        response (dict): The partial response received from the Kubernetes API.

    Raises:
        KeyError: If the observed fields are not present in the Kubernetes response.

    This function iterates through all observed fields and initializes their values if they are not already present in `last_applied_manifest`.
    """
    for key, value in observer_schema.items():
        if key not in response:
            raise KeyError(f"Key '{key}' not found in the Kubernetes response.")
        
        if isinstance(value, dict):
            if key not in last_applied_manifest:
                last_applied_manifest[key] = {}
            update_last_applied_manifest_dict_from_resp(last_applied_manifest[key], value, response[key])
        else:
            if key not in last_applied_manifest:
                last_applied_manifest[key] = response[key]