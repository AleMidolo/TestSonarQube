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
    schema_dict = {}
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            schema_dict[key] = generate_default_observer_schema_dict(value)
        elif isinstance(value, list):
            schema_dict[key] = generate_default_observer_schema_list(value)
        else:
            if first_level and key in ['apiVersion', 'kind', 'metadata']:
                schema_dict[key] = value
            else:
                schema_dict[key] = None
    return schema_dict

def generate_default_observer_schema_list(manifest_list):
    """
    根据 `manifest_list` 文件中的值类型（例如字典和列表），生成新列表中不同元素对应的值。然后返回新的列表。

    与函数 :func:``generate_default_observer_schema_dict`` 一起，该函数被递归调用，用于从部分 Kubernetes 资源中生成默认的 `observer_schema` 的一部分，这些资源分别由 `manifest_dict` 或 `manifest_list` 定义。

    参数:
      manifest_list (list): 部分 Kubernetes 资源。

    返回值:
      list: 生成的部分 `observer_schema`。

    该函数从 `manifest_list` 创建一个新列表，并将所有非列表和非字典的值替换为 `None`。
    """
    schema_list = []
    for item in manifest_list:
        if isinstance(item, dict):
            schema_list.append(generate_default_observer_schema_dict(item))
        elif isinstance(item, list):
            schema_list.append(generate_default_observer_schema_list(item))
        else:
            schema_list.append(None)
    return schema_list