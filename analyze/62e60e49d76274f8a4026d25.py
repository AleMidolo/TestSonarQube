def unit_of_work(metadata=None, timeout=None):
    def decorator(f):
        def wrapper(*args, **kwargs):
            # 验证参数
            if metadata is not None and not isinstance(metadata, dict):
                raise TypeError("metadata must be a dict or None")
            
            if timeout is not None:
                if not isinstance(timeout, (int, float)):
                    raise TypeError("timeout must be a number or None")
                if timeout < 0:
                    raise ValueError("timeout cannot be negative")
            
            # 存储事务配置
            tx_config = {}
            if metadata is not None:
                tx_config["metadata"] = metadata
            if timeout is not None:
                tx_config["timeout"] = timeout
                
            # 执行事务函数
            def run_transaction(tx):
                return f(tx, *args, **kwargs)
                
            # 返回事务配置和事务函数
            return run_transaction, tx_config
            
        return wrapper
        
    # 如果直接传入函数而不是配置参数
    if callable(metadata):
        f = metadata
        metadata = None
        return decorator(f)
        
    return decorator