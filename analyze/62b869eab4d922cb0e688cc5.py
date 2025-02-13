def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    for key, value in observer_schema.items():
        if key not in response:
            raise KeyError(f"Observed field '{key}' is not present in the Kubernetes response")
        if key not in last_applied_manifest:
            last_applied_manifest[key] = response[key]
        if isinstance(value, dict):
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[key], value, response[key]
            )