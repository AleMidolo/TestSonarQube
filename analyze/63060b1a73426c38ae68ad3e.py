import os
import yaml

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    使用 YAML 来读取 `plugin_dir` 中的各种信息，并以字典形式将其返回。
    从插件规范创建一个扁平化的字典

    :param plugin_dir: 插件目录的路径
    :return: 一个包含插件属性的扁平化字典
    """
    plugin_spec_file = os.path.join(plugin_dir, 'plugin.yaml')
    if not os.path.exists(plugin_spec_file):
        raise FileNotFoundError(f"Plugin specification file not found in {plugin_dir}")

    with open(plugin_spec_file, 'r') as file:
        plugin_spec = yaml.safe_load(file)

    def flatten_dict(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    return flatten_dict(plugin_spec)