def validate_fixity(self, fixity, manifest_files):
    """
    验证库存（inventory）中的校验（fixity）块。检查校验块的结构，并保证仅引用了清单中列出的文件。在类中返回`error()`。
    """
    if not isinstance(fixity, dict):
        return self.error("Fixity must be a dictionary.")

    required_keys = ['checksum', 'algorithm', 'files']
    for key in required_keys:
        if key not in fixity:
            return self.error(f"Missing required key: {key}")

    if not isinstance(fixity['files'], list):
        return self.error("Files must be a list.")

    for file in fixity['files']:
        if file not in manifest_files:
            return self.error(f"File {file} is not in the manifest.")

    return True