def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    import os

    # 创建根目录
    if not os.path.exists(self.root_path):
        os.makedirs(self.root_path)

    # 创建必要的子目录和文件
    required_dirs = ['objects', 'extensions']
    for dir_name in required_dirs:
        dir_path = os.path.join(self.root_path, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # 创建 namaste 文件
    namaste_file_path = os.path.join(self.root_path, '0=ocfl_object_1.0')
    with open(namaste_file_path, 'w') as namaste_file:
        namaste_file.write('ocfl_object_1.0\n')

    # 创建 inventory 文件
    inventory_file_path = os.path.join(self.root_path, 'inventory.json')
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
    import json
    with open(inventory_file_path, 'w') as inventory_file:
        json.dump(inventory, inventory_file, indent=2)