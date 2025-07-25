def validate_fixity(self, fixity, manifest_files):
    """
    验证库存（inventory）中的校验（fixity）块。检查校验块的结构，并保证仅引用了清单中列出的文件。在类中返回`error()`。
    """
    if not isinstance(fixity, dict):
        return self.error("Fixity must be a dictionary.")

    required_keys = {'algorithm', 'checksums'}
    if not required_keys.issubset(fixity.keys()):
        return self.error(f"Fixity must contain the keys: {required_keys}")

    if not isinstance(fixity['checksums'], dict):
        return self.error("Checksums must be a dictionary.")

    for file, checksum in fixity['checksums'].items():
        if file not in manifest_files:
            return self.error(f"File '{file}' is not listed in the manifest files.")

        if not isinstance(checksum, str):
            return self.error(f"Checksum for file '{file}' must be a string.")

    return True