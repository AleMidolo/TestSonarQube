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
    
    # 遍历插件目录中的所有 YAML 文件
    for root, dirs, files in os.walk(plugin_dir):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if data:
                        # 将 YAML 文件中的内容扁平化到字典中
                        for key, value in data.items():
                            if key in flattened_dict:
                                if isinstance(flattened_dict[key], list):
                                    flattened_dict[key].append(value)
                                else:
                                    flattened_dict[key] = [flattened_dict[key], value]
                            else:
                                flattened_dict[key] = value
    
    return flattened_dict