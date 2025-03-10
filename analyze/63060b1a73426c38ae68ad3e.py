import os
import yaml

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    使用 YAML 来读取 `plugin_dir` 中的各种信息，并以字典形式将其返回。
    从插件规范创建一个扁平化的字典

    :param plugin_dir: 插件目录的路径
    :return: 一个包含插件属性的扁平化字典
    """
    spec_file = os.path.join(plugin_dir, 'plugin_spec.yaml')
    if not os.path.exists(spec_file):
        raise FileNotFoundError(f"Plugin spec file not found in {plugin_dir}")

    with open(spec_file, 'r') as file:
        spec_data = yaml.safe_load(file)

    # Flatten the dictionary
    flattened_dict = {}
    for key, value in spec_data.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flattened_dict[f"{key}.{sub_key}"] = sub_value
        else:
            flattened_dict[key] = value

    return flattened_dict