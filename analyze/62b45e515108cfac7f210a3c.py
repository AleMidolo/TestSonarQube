def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    import os

    # 定义存储根目录的基本结构
    root_structure = {
        '0=ocfl_1.1': None,  # OCFL版本文件
        'inventory.json': None,  # 库存文件
        'extensions': {},  # 扩展目录
        'objects': {}  # 对象目录
    }

    # 创建根目录
    if not os.path.exists(self.root_path):
        os.makedirs(self.root_path)

    # 创建根目录下的基本结构
    for item, content in root_structure.items():
        path = os.path.join(self.root_path, item)
        if content is None:
            # 创建文件
            with open(path, 'w') as f:
                if item == '0=ocfl_1.1':
                    f.write('ocfl_1.1\n')
                elif item == 'inventory.json':
                    f.write('{}')  # 初始化为空JSON
        else:
            # 创建目录
            os.makedirs(path)