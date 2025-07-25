def validate_fixity(self, fixity, manifest_files):
    """
    验证库存（inventory）中的校验（fixity）块。检查校验块的结构，并保证仅引用了清单中列出的文件。在类中返回`error()`。
    """
    if not isinstance(fixity, dict):
        return self.error("Fixity block must be a dictionary.")
    
    for file_path, checksums in fixity.items():
        if file_path not in manifest_files:
            return self.error(f"File {file_path} in fixity block is not listed in the manifest.")
        
        if not isinstance(checksums, dict):
            return self.error(f"Checksums for file {file_path} must be a dictionary.")
        
        for algorithm, checksum in checksums.items():
            if not isinstance(algorithm, str) or not isinstance(checksum, str):
                return self.error(f"Algorithm and checksum for file {file_path} must be strings.")
    
    return None