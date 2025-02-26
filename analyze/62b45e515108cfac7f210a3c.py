def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    # 创建 OCFL 存储根目录
    os.makedirs(self.root_directory, exist_ok=True)
    
    # 初始化必要的子目录
    os.makedirs(os.path.join(self.root_directory, 'objects'), exist_ok=True)
    os.makedirs(os.path.join(self.root_directory, 'metadata'), exist_ok=True)
    
    # 创建一个初始的配置文件
    config_path = os.path.join(self.root_directory, 'config.json')
    with open(config_path, 'w') as config_file:
        json.dump({"version": "1.0", "created": datetime.now().isoformat()}, config_file)
    
    print("OCFL 存储根目录已创建并初始化。")