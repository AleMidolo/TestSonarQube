def validate_fixity(self, fixity, manifest_files):
    """
    验证库存（inventory）中的校验（fixity）块。检查校验块的结构，并保证仅引用了清单中列出的文件。在类中返回`error()`。
    """
    if not isinstance(fixity, dict):
        return self.error("Fixity block must be a dictionary")
        
    # Check required fields
    required_fields = ["message-digest-algorithm", "message-digest", "message-digest-files"]
    for field in required_fields:
        if field not in fixity:
            return self.error(f"Missing required field '{field}' in fixity block")
            
    # Validate algorithm
    if not isinstance(fixity["message-digest-algorithm"], str):
        return self.error("message-digest-algorithm must be a string")
        
    # Validate digest
    if not isinstance(fixity["message-digest"], str):
        return self.error("message-digest must be a string")
        
    # Validate files list
    if not isinstance(fixity["message-digest-files"], list):
        return self.error("message-digest-files must be a list")
        
    # Check that all referenced files exist in manifest
    for file in fixity["message-digest-files"]:
        if not isinstance(file, str):
            return self.error("All entries in message-digest-files must be strings")
        if file not in manifest_files:
            return self.error(f"File '{file}' referenced in fixity but not found in manifest")
            
    return None