def validate_version_inventories(self, version_dirs):
    """
    每个版本**应当**包含截至该版本的完整清单。  

    同时，记录所有与根清单不同的内容摘要，以便在验证内容时能够检查这些差异。  

    `version_dirs` 是一个包含版本目录名称的数组，并假定按照版本顺序排列（1, 2, 3...）。
    """
    inventory_summaries = {}
    root_inventory = self.load_inventory(version_dirs[0])
    
    for version in version_dirs:
        current_inventory = self.load_inventory(version)
        if not self.is_complete_inventory(current_inventory, root_inventory):
            inventory_summaries[version] = self.get_inventory_diff(current_inventory, root_inventory)
    
    return inventory_summaries

def load_inventory(self, version):
    # 假设这是一个加载版本清单的辅助函数
    pass

def is_complete_inventory(self, current_inventory, root_inventory):
    # 假设这是一个检查当前清单是否完整的辅助函数
    pass

def get_inventory_diff(self, current_inventory, root_inventory):
    # 假设这是一个获取清单差异的辅助函数
    pass