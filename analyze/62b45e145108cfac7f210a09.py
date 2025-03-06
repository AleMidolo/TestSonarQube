def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    检查清单（manifest）中所有需要的摘要（digest）是否存在并被使用。在类中返回 `error()`。
    """
    missing_digests = []
    unused_digests = []
    
    # 检查所有需要的摘要是否存在于清单文件中
    for digest in digests_used:
        if digest not in manifest_files:
            missing_digests.append(digest)
    
    # 检查清单文件中的摘要是否被使用
    for digest in manifest_files:
        if digest not in digests_used:
            unused_digests.append(digest)
    
    # 如果有缺失或未使用的摘要，返回错误
    if missing_digests or unused_digests:
        error_message = ""
        if missing_digests:
            error_message += f"Missing digests: {', '.join(missing_digests)}. "
        if unused_digests:
            error_message += f"Unused digests: {', '.join(unused_digests)}."
        return self.error(error_message)
    
    return None