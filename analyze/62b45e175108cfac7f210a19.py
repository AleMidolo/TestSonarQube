def validate_fixity(self, fixity, manifest_files):
    """
    验证库存（inventory）中的校验（fixity）块。检查校验块的结构，并保证仅引用了清单中列出的文件。在类中返回`error()`。
    """
    if not isinstance(fixity, dict):
        return self.error("Fixity must be a dictionary.")

    required_keys = ['file', 'checksum', 'algorithm']
    for key in required_keys:
        if key not in fixity:
            return self.error(f"Missing required key: {key}")

    if fixity['file'] not in manifest_files:
        return self.error(f"File {fixity['file']} not found in manifest files.")

    if not isinstance(fixity['checksum'], str) or not fixity['checksum']:
        return self.error("Checksum must be a non-empty string.")

    if fixity['algorithm'] not in ['md5', 'sha1', 'sha256']:
        return self.error("Invalid algorithm. Must be one of: md5, sha1, sha256.")

    return True