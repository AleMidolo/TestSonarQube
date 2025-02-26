def update_last_applied_manifest_dict_from_resp(last_applied_manifest, observer_schema, response):
    """
    与函数 :func:``update_last_applied_manifest_list_from_resp`` 一起，该函数被递归调用，用于从部分 Kubernetes 响应中更新部分 ``last_applied_manifest``。

    参数:
      last_applied_manifest (list): 正在更新的部分 ``last_applied_manifest``。
      observer_schema (list): 部分 ``observer_schema``。
      response (list): 来自 Kubernetes API 的部分响应。

    异常:
      KeyError: 如果在 Kubernetes 响应中未找到观察字段，则抛出此异常。

    此函数会遍历所有观察到的字段，如果它们尚未在 `last_applied_manifest` 中初始化，则会为其初始化值。
    """
    for field in observer_schema:
        if field not in last_applied_manifest:
            if field not in response:
                raise KeyError(f"Field '{field}' not found in response.")
            last_applied_manifest[field] = response[field]
        elif isinstance(last_applied_manifest[field], dict) and isinstance(response[field], dict):
            update_last_applied_manifest_dict_from_resp(last_applied_manifest[field], observer_schema[field], response[field])
    return last_applied_manifest