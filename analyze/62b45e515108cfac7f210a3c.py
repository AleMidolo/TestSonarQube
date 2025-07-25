def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    # 创建根目录
    os.makedirs(self.root_path, exist_ok=True)
    
    # 创建 namaste 文件
    namaste_path = os.path.join(self.root_path, "0=ocfl_1.0")
    with open(namaste_path, "w") as f:
        f.write("ocfl_1.0")
        
    # 创建 ocfl_layout.json 文件
    layout = {
        "extension": "000",
        "description": "OCFL Storage Root",
        "layout": {
            "type": "flat",
            "pattern": "^[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]{2}/.*$"
        }
    }
    
    layout_path = os.path.join(self.root_path, "ocfl_layout.json") 
    with open(layout_path, "w") as f:
        json.dump(layout, f, indent=2)
        
    # 创建对象目录
    objects_path = os.path.join(self.root_path, "objects")
    os.makedirs(objects_path, exist_ok=True)