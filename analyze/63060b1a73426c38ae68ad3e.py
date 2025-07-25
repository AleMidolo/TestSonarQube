import os
import yaml

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    使用 YAML 来读取 `plugin_dir` 中的各种信息，并以字典形式将其返回。
    从插件规范创建一个扁平化的字典

    :param plugin_dir: 插件目录的路径
    :return: 一个包含插件属性的扁平化字典
    """
    flatten_dict = {}

    for root, _, files in os.walk(plugin_dir):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        content = yaml.safe_load(f)
                        if isinstance(content, dict):
                            for key, value in content.items():
                                flatten_dict[key] = value
                    except yaml.YAMLError as e:
                        print(f"Error reading {file_path}: {e}")

    return flatten_dict