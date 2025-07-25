import os

def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    # 创建根目录
    os.makedirs(self.root_path, exist_ok=True)
    
    # 创建必要的子目录和文件
    os.makedirs(os.path.join(self.root_path, '0=ocfl_1.1'), exist_ok=True)
    os.makedirs(os.path.join(self.root_path, 'extensions'), exist_ok=True)
    os.makedirs(os.path.join(self.root_path, 'objects'), exist_ok=True)
    
    # 创建 namaste 文件
    with open(os.path.join(self.root_path, '0=ocfl_1.1'), 'w') as f:
        f.write('ocfl_1.1\n')
    
    # 创建 ocfl_layout.json 文件
    with open(os.path.join(self.root_path, 'ocfl_layout.json'), 'w') as f:
        f.write('{"type": "https://ocfl.io/1.1/spec/#layout-hierarchical"}\n')