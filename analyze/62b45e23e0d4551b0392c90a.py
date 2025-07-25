def validate_version_inventories(self, version_dirs):
    """
    每个版本**应当**包含截至该版本的完整清单。  

    同时，记录所有与根清单不同的内容摘要，以便在验证内容时能够检查这些差异。  

    `version_dirs` 是一个包含版本目录名称的数组，并假定按照版本顺序排列（1, 2, 3...）。
    """
    # 存储每个版本的清单差异
    version_diffs = {}
    
    # 获取根目录清单
    root_inventory = self.get_root_inventory()
    
    # 遍历每个版本目录
    for version in version_dirs:
        version_inventory = self.get_version_inventory(version)
        
        # 检查是否包含完整清单
        if not version_inventory:
            raise ValueError(f"Version {version} missing complete inventory")
            
        # 与根清单比较,记录差异
        diffs = {}
        for file_path, checksum in version_inventory.items():
            if file_path not in root_inventory:
                diffs[file_path] = {'status': 'added', 'checksum': checksum}
            elif root_inventory[file_path] != checksum:
                diffs[file_path] = {
                    'status': 'modified',
                    'old_checksum': root_inventory[file_path],
                    'new_checksum': checksum
                }
                
        for file_path in root_inventory:
            if file_path not in version_inventory:
                diffs[file_path] = {
                    'status': 'deleted',
                    'old_checksum': root_inventory[file_path]
                }
                
        # 存储该版本的差异
        if diffs:
            version_diffs[version] = diffs
            
    return version_diffs