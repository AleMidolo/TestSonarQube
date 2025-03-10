def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    检查清单（manifest）中所有需要的摘要（digest）是否存在并被使用。在类中返回 `error()`。
    """
    for manifest_file in manifest_files:
        if not manifest_file.get('digest'):
            return self.error(f"Digest missing in manifest file: {manifest_file}")
    
    for digest in digests_used:
        if not any(manifest_file.get('digest') == digest for manifest_file in manifest_files):
            return self.error(f"Digest not found in any manifest file: {digest}")
    
    return None