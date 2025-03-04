def get_plugin_spec_flatten_dict(plugin_dir):
    """
    使用 YAML 来读取 `plugin_dir` 中的各种信息，并以字典形式将其返回。
    从插件规范创建一个扁平化的字典

    :param plugin_dir: 插件目录的路径 
    :return: 一个包含插件属性的扁平化字典
    """
    import os
    import yaml
    
    # 初始化结果字典
    result = {}
    
    # 读取插件目录下的 plugin.yaml 文件
    spec_file = os.path.join(plugin_dir, 'plugin.yaml')
    if not os.path.exists(spec_file):
        return result
        
    # 读取 YAML 文件
    with open(spec_file, 'r', encoding='utf-8') as f:
        try:
            spec = yaml.safe_load(f)
        except yaml.YAMLError:
            return result
            
    def flatten_dict(d, parent_key='', sep='.'):
        """递归地将嵌套字典扁平化"""
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    # 扁平化字典
    if isinstance(spec, dict):
        result = flatten_dict(spec)
    
    return result