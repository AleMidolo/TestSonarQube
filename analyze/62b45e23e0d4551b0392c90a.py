def validate_version_inventories(self, version_dirs):
    """
    每个版本**应当**包含截至该版本的完整清单。  

    同时，记录所有与根清单不同的内容摘要，以便在验证内容时能够检查这些差异。  

    `version_dirs` 是一个包含版本目录名称的数组，并假定按照版本顺序排列（1, 2, 3...)。
    """
    root_inventory = self._load_inventory("root")  # 假设根清单存储在根目录
    discrepancies = {}

    for version_dir in version_dirs:
        version_inventory = self._load_inventory(version_dir)
        if not self._is_complete_inventory(version_inventory, root_inventory):
            raise ValueError(f"Inventory in {version_dir} is not complete.")

        diff = self._compare_inventories(version_inventory, root_inventory)
        if diff:
            discrepancies[version_dir] = diff

    return discrepancies

def _load_inventory(self, directory):
    """
    从指定目录加载清单。
    """
    # 假设清单是一个 JSON 文件
    import json
    with open(f"{directory}/inventory.json", "r") as f:
        return json.load(f)

def _is_complete_inventory(self, version_inventory, root_inventory):
    """
    检查版本清单是否包含根清单的所有内容。
    """
    return all(item in version_inventory for item in root_inventory)

def _compare_inventories(self, version_inventory, root_inventory):
    """
    比较版本清单和根清单，返回差异。
    """
    diff = {}
    for key in root_inventory:
        if key not in version_inventory:
            diff[key] = "Missing"
        elif version_inventory[key] != root_inventory[key]:
            diff[key] = {
                "root_value": root_inventory[key],
                "version_value": version_inventory[key]
            }
    return diff