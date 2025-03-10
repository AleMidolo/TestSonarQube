def validate_version_inventories(self, version_dirs):
    """
    每个版本**应当**包含截至该版本的完整清单。  

    同时，记录所有与根清单不同的内容摘要，以便在验证内容时能够检查这些差异。  

    `version_dirs` 是一个包含版本目录名称的数组，并假定按照版本顺序排列（1, 2, 3...）。
    """
    root_inventory = set()  # 根清单
    differences = {}  # 记录每个版本与根清单的差异

    for version_dir in version_dirs:
        # 假设每个版本目录下有一个名为 'inventory.txt' 的文件，包含该版本的清单
        with open(f"{version_dir}/inventory.txt", 'r') as file:
            current_inventory = set(line.strip() for line in file)

        # 如果是第一个版本，将其作为根清单
        if not root_inventory:
            root_inventory = current_inventory
            differences[version_dir] = "Root inventory"
            continue

        # 计算当前版本与根清单的差异
        diff = current_inventory - root_inventory
        if diff:
            differences[version_dir] = diff
        else:
            differences[version_dir] = "No differences"

    return differences