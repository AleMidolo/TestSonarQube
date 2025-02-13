def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    for schema_item in observer_schema:
        field_name = schema_item['name']
        if field_name not in last_applied_manifest:
            last_applied_manifest[field_name] = None  # Initialize with None or appropriate default

    for resp_item in response:
        for schema_item in observer_schema:
            field_name = schema_item['name']
            if field_name in resp_item:
                last_applied_manifest[field_name] = resp_item[field_name]

    return last_applied_manifest