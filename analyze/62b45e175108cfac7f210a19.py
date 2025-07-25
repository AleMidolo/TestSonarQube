def validate_fixity(self, fixity, manifest_files):
    """
    验证库存（inventory）中的校验（fixity）块。检查校验块的结构，并保证仅引用了清单中列出的文件。在类中返回`error()`。
    """
    if not isinstance(fixity, dict):
        return self.error("Fixity must be a dictionary.")

    required_keys = ['algorithm', 'checksums']
    for key in required_keys:
        if key not in fixity:
            return self.error(f"Missing required key: {key}")

    if not isinstance(fixity['checksums'], dict):
        return self.error("Checksums must be a dictionary.")

    for file, checksum in fixity['checksums'].items():
        if file not in manifest_files:
            return self.error(f"File {file} is not listed in the manifest.")
        if not isinstance(checksum, str):
            return self.error(f"Checksum for {file} must be a string.")

    return True