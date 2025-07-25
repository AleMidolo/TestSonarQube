def validate_version_inventories(self, version_dirs):
    """
    每个版本**应当**包含截至该版本的完整清单。  

    同时，记录所有与根清单不同的内容摘要，以便在验证内容时能够检查这些差异。  

    `version_dirs` 是一个包含版本目录名称的数组，并假定按照版本顺序排列（1, 2, 3...)。
    """
    root_inventory = set()  # 假设根清单是一个集合
    differences = {}  # 用于存储每个版本与根清单的差异

    for version_dir in version_dirs:
        # 假设每个版本目录下有一个名为 'inventory.txt' 的文件，包含该版本的清单
        with open(f"{version_dir}/inventory.txt", 'r') as file:
            current_inventory = set(file.read().splitlines())
        
        # 检查当前清单是否包含根清单的所有内容
        if not root_inventory.issubset(current_inventory):
            raise ValueError(f"版本 {version_dir} 的清单不完整，缺少根清单中的某些内容。")
        
        # 记录与根清单的差异
        differences[version_dir] = current_inventory - root_inventory
        
        # 更新根清单为当前版本的清单
        root_inventory = current_inventory

    return differences