def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    检查清单（manifest）中所有需要的摘要（digest）是否存在并被使用。在类中返回 `error()`。
    """
    for manifest_file in manifest_files:
        if manifest_file not in digests_used:
            return self.error(f"Digest for {manifest_file} is missing or not used.")
    return None