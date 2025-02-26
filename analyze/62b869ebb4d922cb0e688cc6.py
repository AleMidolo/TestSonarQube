def update_last_applied_manifest_list_from_resp(last_applied_manifest, observer_schema, response):
    """
    与函数 :func:``update_last_applied_manifest_dict_from_resp`` 一起，该函数被递归调用，来从部分 Kubernetes 响应中更新部分 ``last_applied_manifest``。

    参数:
      last_applied_manifest (list): 正在更新的部分 ``last_applied_manifest``。
      observer_schema (list): 部分 ``observer_schema``。
      response (list): 来自 Kubernetes API 的部分响应。

    此函数会遍历所有观察到的字段，如果它们尚未在 `last_applied_manifest` 中初始化，则会为其初始化值。
    """
    for schema in observer_schema:
        field = schema.get('field')
        if field not in last_applied_manifest:
            last_applied_manifest[field] = None  # Initialize with None or appropriate default

        # If the field is a list, we need to update it based on the response
        if isinstance(last_applied_manifest[field], list):
            last_applied_manifest[field] = response.get(field, [])

    return last_applied_manifest