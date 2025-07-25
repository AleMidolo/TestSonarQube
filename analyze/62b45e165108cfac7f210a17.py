def get_logical_path_map(inventory, version):
    """
    返回库存（inventory）中各状态的文件路径，并以字典类型表示。
    获取库存中某个版本的状态逻辑路径到磁盘文件的映射。

    返回一个字典：`logical_path_in_state -> set(content_files)`

    集合`content_files`可能包含对比所描述版本更高版本中重复文件的引用。
    """
    logical_path_map = {}
    
    for logical_path, file_versions in inventory.items():
        content_files = set()
        for file_version, file_path in file_versions.items():
            if file_version <= version:
                content_files.add(file_path)
        if content_files:
            logical_path_map[logical_path] = content_files
    
    return logical_path_map