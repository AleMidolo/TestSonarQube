def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    # 创建 OCFL 存储根目录
    import os

    root_directory = "ocfl_root"  # OCFL 存储根目录名称
    if not os.path.exists(root_directory):
        os.makedirs(root_directory)  # 创建目录

    # 初始化 OCFL 结构
    version_file = os.path.join(root_directory, "version.txt")
    with open(version_file, 'w') as f:
        f.write("OCFL Version 1.0\n")  # 写入版本信息

    # 其他初始化操作可以在这里添加
    print(f"OCFL 存储根目录 '{root_directory}' 已创建并初始化。")