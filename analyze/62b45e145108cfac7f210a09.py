def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    检查清单（manifest）中所有需要的摘要（digest）是否存在并被使用。在类中返回 `error()`。
    """
    # 遍历所有清单文件
    for manifest in manifest_files:
        # 获取清单中的摘要列表
        manifest_digests = set()
        try:
            for layer in manifest.get('layers', []):
                if 'digest' in layer:
                    manifest_digests.add(layer['digest'])
            if 'config' in manifest and 'digest' in manifest['config']:
                manifest_digests.add(manifest['config']['digest'])
        except (KeyError, TypeError):
            return self.error(f"无法从清单中解析摘要: {manifest}")

        # 检查所有摘要是否都被使用
        unused_digests = manifest_digests - set(digests_used)
        if unused_digests:
            return self.error(f"以下摘要存在于清单中但未被使用: {unused_digests}")

        # 检查所有使用的摘要是否都存在于清单中
        missing_digests = set(digests_used) - manifest_digests
        if missing_digests:
            return self.error(f"以下使用的摘要在清单中不存在: {missing_digests}")

    return None