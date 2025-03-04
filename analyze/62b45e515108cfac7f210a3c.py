def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    # 创建根目录
    os.makedirs(self.root_path, exist_ok=True)
    
    # 创建 0=ocfl_1.0 命名空间声明文件
    namespace_file = os.path.join(self.root_path, "0=ocfl_1.0")
    with open(namespace_file, "w") as f:
        f.write("")
        
    # 创建 ocfl_layout.json 文件
    layout_file = os.path.join(self.root_path, "ocfl_layout.json")
    layout_content = {
        "extension": "000",
        "description": "OCFL Storage Root",
        "layout": {
            "type": "flat",
            "pattern": "{object-id}"
        }
    }
    
    with open(layout_file, "w") as f:
        json.dump(layout_content, f, indent=2)
        
    # 创建空的 extensions 目录
    extensions_dir = os.path.join(self.root_path, "extensions")
    os.makedirs(extensions_dir, exist_ok=True)