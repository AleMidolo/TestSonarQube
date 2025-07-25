def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    # 创建 OCFL 存储根目录
    import os

    root_directory = "ocfl_root"  # OCFL 存储根目录名称
    if not os.path.exists(root_directory):
        os.makedirs(root_directory)  # 创建目录
        print(f"OCFL 存储根目录 '{root_directory}' 已创建。")
    else:
        print(f"OCFL 存储根目录 '{root_directory}' 已存在。")

    # 初始化其他必要的文件或配置
    config_file = os.path.join(root_directory, "config.json")
    if not os.path.exists(config_file):
        with open(config_file, 'w') as f:
            f.write('{}')  # 创建一个空的配置文件
        print(f"配置文件 '{config_file}' 已创建。")
    else:
        print(f"配置文件 '{config_file}' 已存在。")