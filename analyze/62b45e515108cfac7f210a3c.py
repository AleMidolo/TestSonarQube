def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    import os

    # 创建根目录
    if not os.path.exists('ocfl_root'):
        os.makedirs('ocfl_root')
    
    # 创建必要的子目录和文件
    os.makedirs('ocfl_root/0=ocfl_object_1.0')
    with open('ocfl_root/0=ocfl_object_1.0/inventory.json', 'w') as f:
        f.write('{}')
    
    # 创建 namaste 文件
    with open('ocfl_root/0=ocfl_object_1.0/0=ocfl_object_1.0', 'w') as f:
        f.write('ocfl_object_1.0')