def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    import os

    # 创建根目录
    if not os.path.exists(self.root_path):
        os.makedirs(self.root_path)

    # 创建必要的子目录和文件
    required_dirs = ['0=ocfl_1.0', 'extensions', 'logs']
    for dir_name in required_dirs:
        dir_path = os.path.join(self.root_path, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # 创建并写入 namaste 文件
    namaste_file_path = os.path.join(self.root_path, '0=ocfl_1.0')
    with open(namaste_file_path, 'w') as namaste_file:
        namaste_file.write('ocfl_1.0\n')

    # 创建并写入 inventory.json 文件
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
    inventory_file_path = os.path.join(self.root_path, 'inventory.json')
    with open(inventory_file_path, 'w') as inventory_file:
        import json
        json.dump(inventory, inventory_file, indent=2)

    # 创建并写入 inventory.json.sha512 文件
    import hashlib
    with open(inventory_file_path, 'rb') as f:
        sha512_hash = hashlib.sha512(f.read()).hexdigest()
    hash_file_path = os.path.join(self.root_path, 'inventory.json.sha512')
    with open(hash_file_path, 'w') as hash_file:
        hash_file.write(sha512_hash)