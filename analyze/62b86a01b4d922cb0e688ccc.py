def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    """
    根据 `manifest_dict` 文件中的值类型（例如字典和列表），生成新字典中不同键对应的值。然后返回新的字典。

    与函数 :func:``generate_default_observer_schema_list`` 一起，该函数被递归调用，用于从部分 Kubernetes 资源中生成默认的 `observer_schema` 的一部分，这些资源分别由 `manifest_dict` 或 `manifest_list` 定义。

    参数:
      manifest_dict (dict): 部分 Kubernetes 资源。
      first_level (bool, 可选): 如果为真，表示该字典代表 Kubernetes 资源的完整 `observer_schema`。

    返回值:
      dict: 生成的部分 `observer_schema`。

    该函数从 `manifest_dict` 创建一个新字典，并将所有非列表和非字典的值替换为 `None`。

    如果是 `first_level` 字典（比如资源的完整 `observer_schema`），则标识字段的值会从 manifest 文件中复制。
    """
    observer_schema = {}
    
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value, first_level=False)
        elif isinstance(value, list):
            observer_schema[key] = [generate_default_observer_schema_dict(item, first_level=False) if isinstance(item, dict) else None for item in value]
        else:
            if first_level and key == 'metadata':
                observer_schema[key] = value  # Copy metadata as is for first level
            else:
                observer_schema[key] = None  # Replace non-dict and non-list values with None

    return observer_schema