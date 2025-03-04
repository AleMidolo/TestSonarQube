def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    检查清单（manifest）中所有需要的摘要（digest）是否存在并被使用。在类中返回 `error()`。
    """
    # 存储所有在清单文件中找到的摘要
    manifest_digests = set()
    
    # 遍历所有清单文件
    for manifest in manifest_files:
        # 如果清单中有 'digest' 字段
        if 'digest' in manifest:
            manifest_digests.add(manifest['digest'])
            
    # 检查是否所有使用的摘要都在清单中存在
    for digest in digests_used:
        if digest not in manifest_digests:
            return self.error(f"Digest {digest} is used but not present in manifest files")
            
    # 检查是否所有清单中的摘要都被使用
    for digest in manifest_digests:
        if digest not in digests_used:
            return self.error(f"Digest {digest} is in manifest but never used")
            
    # 如果所有检查都通过，返回None表示没有错误
    return None