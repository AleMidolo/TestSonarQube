import os
import yaml

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    使用 YAML 来读取 `plugin_dir` 中的各种信息，并以字典形式将其返回。
    从插件规范创建一个扁平化的字典

    :param plugin_dir: 插件目录的路径
    :return: 一个包含插件属性的扁平化字典
    """
    flattened_dict = {}
    
    # 遍历插件目录中的所有文件
    for root, dirs, files in os.walk(plugin_dir):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = yaml.safe_load(f)
                        if isinstance(data, dict):
                            # 将嵌套字典扁平化
                            for key, value in data.items():
                                if isinstance(value, dict):
                                    for sub_key, sub_value in value.items():
                                        flattened_dict[f"{key}.{sub_key}"] = sub_value
                                else:
                                    flattened_dict[key] = value
                    except yaml.YAMLError as e:
                        print(f"Error parsing YAML file {file_path}: {e}")
    
    return flattened_dict