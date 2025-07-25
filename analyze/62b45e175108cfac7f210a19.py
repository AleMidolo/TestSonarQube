def validate_fixity(self, fixity, manifest_files):
    """
    验证库存（inventory）中的校验（fixity）块。检查校验块的结构，并保证仅引用了清单中列出的文件。在类中返回`error()`。
    """
    if not isinstance(fixity, dict):
        return self.error("Fixity block must be a dictionary")
        
    # Check required fields
    required_fields = ["message-digest-algorithm", "message-digest"]
    for field in required_fields:
        if field not in fixity:
            return self.error(f"Missing required field '{field}' in fixity block")
            
    # Validate algorithm field
    if not isinstance(fixity["message-digest-algorithm"], str):
        return self.error("message-digest-algorithm must be a string")
        
    # Validate digest field
    digests = fixity["message-digest"]
    if not isinstance(digests, list):
        return self.error("message-digest must be a list")
        
    # Check each digest entry
    for digest in digests:
        if not isinstance(digest, dict):
            return self.error("Each message-digest entry must be a dictionary")
            
        if "file" not in digest or "hash" not in digest:
            return self.error("Each message-digest entry must have 'file' and 'hash' fields")
            
        if not isinstance(digest["file"], str) or not isinstance(digest["hash"], str):
            return self.error("Digest file and hash values must be strings")
            
        # Verify file exists in manifest
        if digest["file"] not in manifest_files:
            return self.error(f"Digest references non-existent file: {digest['file']}")
            
    return None