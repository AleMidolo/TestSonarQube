def update_last_applied_manifest_list_from_resp(last_applied_manifest, observer_schema, response):
    """
    与函数 :func:``update_last_applied_manifest_dict_from_resp`` 一起，该函数被递归调用，来从部分 Kubernetes 响应中更新部分 ``last_applied_manifest``。

    参数:
      last_applied_manifest (list): 正在更新的部分 ``last_applied_manifest``。
      observer_schema (list): 部分 ``observer_schema``。
      response (list): 来自 Kubernetes API 的部分响应。

    此函数会遍历所有观察到的字段，如果它们尚未在 `last_applied_manifest` 中初始化，则会为其初始化值。
    """
    for i, (schema_item, resp_item) in enumerate(zip(observer_schema, response)):
        if isinstance(schema_item, dict) and isinstance(resp_item, dict):
            if i >= len(last_applied_manifest):
                last_applied_manifest.append({})
            update_last_applied_manifest_dict_from_resp(last_applied_manifest[i], schema_item, resp_item)
        elif isinstance(schema_item, list) and isinstance(resp_item, list):
            if i >= len(last_applied_manifest):
                last_applied_manifest.append([])
            update_last_applied_manifest_list_from_resp(last_applied_manifest[i], schema_item, resp_item)
        else:
            if i >= len(last_applied_manifest):
                last_applied_manifest.append(resp_item)
            else:
                last_applied_manifest[i] = resp_item