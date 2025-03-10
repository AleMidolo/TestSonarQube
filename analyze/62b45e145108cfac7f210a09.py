def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    检查清单（manifest）中所有需要的摘要（digest）是否存在并被使用。在类中返回 `error()`。
    """
    # 假设 manifest_files 是一个字典，键为文件名，值为摘要列表
    # digests_used 是一个集合，包含所有被使用的摘要
    
    # 检查所有清单文件中的摘要是否都存在
    for file_name, digests in manifest_files.items():
        for digest in digests:
            if digest not in digests_used:
                return self.error(f"Digest {digest} from file {file_name} is not used.")
    
    # 检查所有被使用的摘要是否都在清单文件中
    for digest in digests_used:
        found = False
        for file_name, digests in manifest_files.items():
            if digest in digests:
                found = True
                break
        if not found:
            return self.error(f"Digest {digest} is used but not found in any manifest file.")
    
    # 如果没有问题，返回 None 或成功信息
    return None