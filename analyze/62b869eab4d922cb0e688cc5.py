def update_last_applied_manifest_dict_from_resp(last_applied_manifest, observer_schema, response):
    """
    与函数 :func:``update_last_applied_manifest_list_from_resp`` 一起，该函数被递归调用，用于从部分 Kubernetes 响应中更新部分 ``last_applied_manifest``。

    参数:
      last_applied_manifest (dict): 正在更新的部分 ``last_applied_manifest``。
      observer_schema (dict): 部分 ``observer_schema``。
      response (dict): 来自 Kubernetes API 的部分响应。

    异常:
      KeyError: 如果在 Kubernetes 响应中未找到观察字段，则抛出此异常。

    此函数会遍历所有观察到的字段，如果它们尚未在 `last_applied_manifest` 中初始化，则会为其初始化值。
    """
    for key, schema in observer_schema.items():
        if key not in response:
            raise KeyError(f"Key '{key}' not found in the Kubernetes response.")
        
        if key not in last_applied_manifest:
            if isinstance(schema, dict):
                last_applied_manifest[key] = {}
            elif isinstance(schema, list):
                last_applied_manifest[key] = []
            else:
                last_applied_manifest[key] = response[key]
        
        if isinstance(schema, dict):
            update_last_applied_manifest_dict_from_resp(last_applied_manifest[key], schema, response[key])
        elif isinstance(schema, list):
            update_last_applied_manifest_list_from_resp(last_applied_manifest[key], schema, response[key])
        else:
            last_applied_manifest[key] = response[key]