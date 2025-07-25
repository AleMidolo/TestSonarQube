def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    验证存储根层次结构。

    返回:
        num_objects (int): 检查的对象数量。
        good_objects (int): 检查后被认为有效的对象数量。
    """
    num_objects = 0
    good_objects = 0
    
    # 遍历所有存储对象
    for obj in self.get_all_objects():
        num_objects += 1
        
        try:
            # 验证对象
            if validate_objects:
                obj.validate()
                
            # 检查摘要
            if check_digests:
                stored_digest = obj.get_digest()
                calculated_digest = obj.calculate_digest()
                if stored_digest != calculated_digest:
                    if show_warnings:
                        print(f"Warning: Digest mismatch for object {obj.id}")
                    continue
                    
            good_objects += 1
            
        except Exception as e:
            if show_warnings:
                print(f"Warning: Failed to validate object {obj.id}: {str(e)}")
            continue
            
    return num_objects, good_objects