import os

def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    # 创建根目录
    os.makedirs(self.root_path, exist_ok=True)
    
    # 创建必要的子目录和文件
    os.makedirs(os.path.join(self.root_path, '0=ocfl_1.0'), exist_ok=True)
    os.makedirs(os.path.join(self.root_path, 'extensions'), exist_ok=True)
    os.makedirs(os.path.join(self.root_path, 'objects'), exist_ok=True)
    
    # 创建 namaste 文件
    with open(os.path.join(self.root_path, '0=ocfl_1.0'), 'w') as f:
        f.write('ocfl_1.0\n')
    
    # 创建 inventory.json 文件
    inventory = {
        "id": "urn:uuid:12345678-1234-5678-1234-567812345678",
        "type": "Object",
        "digestAlgorithm": "sha512",
        "head": "v1",
        "versions": {
            "v1": {
                "created": "2023-10-01T00:00:00Z",
                "state": {},
                "message": "Initial version"
            }
        }
    }
    
    with open(os.path.join(self.root_path, 'inventory.json'), 'w') as f:
        json.dump(inventory, f, indent=2)