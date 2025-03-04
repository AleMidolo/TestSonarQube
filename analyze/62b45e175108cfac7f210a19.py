def validate_fixity(self, fixity, manifest_files):
    """
    验证库存（inventory）中的校验（fixity）块。检查校验块的结构，并保证仅引用了清单中列出的文件。在类中返回`error()`。
    """
    if not isinstance(fixity, dict):
        return self.error("Fixity block must be a dictionary")
        
    # Check required fields
    required_fields = ["message-digest-algorithm", "message-digest", "message-digest-file"]
    for field in required_fields:
        if field not in fixity:
            return self.error(f"Missing required field '{field}' in fixity block")
            
    # Validate algorithm
    if not isinstance(fixity["message-digest-algorithm"], str):
        return self.error("message-digest-algorithm must be a string")
        
    # Validate digest
    if not isinstance(fixity["message-digest"], str):
        return self.error("message-digest must be a string")
        
    # Validate digest files
    if not isinstance(fixity["message-digest-file"], list):
        return self.error("message-digest-file must be a list")
        
    # Check that all referenced files exist in manifest
    for digest_file in fixity["message-digest-file"]:
        if not isinstance(digest_file, str):
            return self.error("All message-digest-file entries must be strings")
        if digest_file not in manifest_files:
            return self.error(f"File '{digest_file}' referenced in fixity block not found in manifest")
            
    return None