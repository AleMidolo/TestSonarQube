def get_logical_path_map(inventory, version):
    """
    返回库存（inventory）中各状态的文件路径，并以字典类型表示。
    获取库存中某个版本的状态逻辑路径到磁盘文件的映射。

    返回一个字典：`logical_path_in_state -> set(content_files)`

    集合`content_files`可能包含对比所描述版本更高版本中重复文件的引用。
    """
    logical_path_map = {}
    
    # 遍历库存中的所有版本
    for ver in inventory.versions:
        # 只处理指定版本及其之前的版本
        if ver > version:
            continue
            
        # 遍历该版本中的所有文件
        for logical_path, content_file in ver.files.items():
            # 如果逻辑路径不在映射中，创建一个新集合
            if logical_path not in logical_path_map:
                logical_path_map[logical_path] = set()
                
            # 将内容文件添加到对应逻辑路径的集合中
            logical_path_map[logical_path].add(content_file)
    
    return logical_path_map