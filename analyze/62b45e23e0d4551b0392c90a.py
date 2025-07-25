def validate_version_inventories(self, version_dirs):
    """
    每个版本**应当**包含截至该版本的完整清单。  

    同时，记录所有与根清单不同的内容摘要，以便在验证内容时能够检查这些差异。  

    `version_dirs` 是一个包含版本目录名称的数组，并假定按照版本顺序排列（1, 2, 3...)。
    """
    root_inventory = self.get_root_inventory()  # 假设有一个方法获取根清单
    differences = {}

    for version_dir in version_dirs:
        version_inventory = self.get_version_inventory(version_dir)  # 假设有一个方法获取版本清单
        if not self.is_complete_inventory(version_inventory, root_inventory):
            raise ValueError(f"Inventory in {version_dir} is not complete.")
        
        diff = self.compare_inventories(version_inventory, root_inventory)  # 假设有一个方法比较清单
        if diff:
            differences[version_dir] = diff

    return differences