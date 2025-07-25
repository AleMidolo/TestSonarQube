def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    检查清单（manifest）中所有需要的摘要（digest）是否存在并被使用。在类中返回 `error()`。
    """
    missing_digests = []
    for manifest in manifest_files:
        for digest in digests_used:
            if digest not in manifest:
                missing_digests.append(digest)

    if missing_digests:
        return self.error(f"Missing digests: {', '.join(missing_digests)}")
    return None