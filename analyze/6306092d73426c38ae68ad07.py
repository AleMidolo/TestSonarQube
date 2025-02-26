def validate_requires_args(self, args):
    """
    检查是否提供了所有必需的参数。
    """
    required_args = self.get_required_args()  # 假设有一个方法获取必需参数
    missing_args = [arg for arg in required_args if arg not in args]
    
    if missing_args:
        raise ValueError(f"缺少必需的参数: {', '.join(missing_args)}")
    
    return True