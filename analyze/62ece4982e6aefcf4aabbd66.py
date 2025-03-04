def was_processed(processed, path_name, verbose):
    """
    检查文件或目录是否已被处理。

    为了防止递归，将路径名扩展为绝对路径。调用此函数时，提供一个用于存储所有条目的集合以及需要测试的条目。如果该条目已存在于集合中，则报告问题并返回真。否则，将条目添加到集合并返回假以允许处理该路径。

    参数：
        processed：用于存储已处理路径名的集合
        path_name：目录或文件的路径
        verbose：如果需要详细输出，则为真

    返回值：
        如果路径已在集合中，则返回真。否则返回假。
    """
    import os
    
    # 将路径转换为绝对路径
    abs_path = os.path.abspath(path_name)
    
    # 检查路径是否已在集合中
    if abs_path in processed:
        if verbose:
            print(f"Warning: {path_name} has already been processed")
        return True
        
    # 将新路径添加到集合中
    processed.add(abs_path)
    return False