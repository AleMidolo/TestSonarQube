import os
import yaml

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    使用 YAML 来读取 `plugin_dir` 中的各种信息，并以字典形式将其返回。
    从插件规范创建一个扁平化的字典

    :param plugin_dir: 插件目录的路径
    :return: 一个包含插件属性的扁平化字典
    """
    plugin_spec_file = os.path.join(plugin_dir, 'plugin_spec.yaml')
    if not os.path.exists(plugin_spec_file):
        raise FileNotFoundError(f"Plugin spec file not found in {plugin_dir}")

    with open(plugin_spec_file, 'r') as file:
        plugin_spec = yaml.safe_load(file)

    # Flatten the dictionary
    flattened_dict = {}
    def flatten(d, parent_key='', sep='.'):
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                flatten(v, new_key, sep=sep)
            else:
                flattened_dict[new_key] = v
        return flattened_dict

    return flatten(plugin_spec)