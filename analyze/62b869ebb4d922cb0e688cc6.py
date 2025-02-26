def update_last_applied_manifest_list_from_resp(last_applied_manifest, observer_schema, response):
    """
    与函数 :func:``update_last_applied_manifest_dict_from_resp`` 一起，该函数被递归调用，来从部分 Kubernetes 响应中更新部分 ``last_applied_manifest``。

    参数:
      last_applied_manifest (list): 正在更新的部分 ``last_applied_manifest``。
      observer_schema (list): 部分 ``observer_schema``。
      response (list): 来自 Kubernetes API 的部分响应。

    此函数会遍历所有观察到的字段，如果它们尚未在 `last_applied_manifest` 中初始化，则会为其初始化值。
    """
    for schema_item in observer_schema:
        field_name = schema_item.get('name')
        if field_name not in last_applied_manifest:
            last_applied_manifest[field_name] = None  # Initialize with None or appropriate default

        # If the schema item has nested fields, we need to handle them recursively
        if 'nested' in schema_item:
            nested_schema = schema_item['nested']
            nested_response = response.get(field_name, {})
            update_last_applied_manifest_list_from_resp(last_applied_manifest[field_name], nested_schema, nested_response)

    return last_applied_manifest