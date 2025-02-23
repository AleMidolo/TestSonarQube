def inject_config(self):
    """
    如果 `os.environ` 中不存在 `ANSIBLE_CONFIG` 属性，则将其设置为 `self.ansible_config_path`。

    如果配置路径的环境变量未定义，则进行设置。
    """
    import os
    
    if 'ANSIBLE_CONFIG' not in os.environ:
        os.environ['ANSIBLE_CONFIG'] = self.ansible_config_path