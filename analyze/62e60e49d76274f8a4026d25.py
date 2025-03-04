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
            
            # 存储事务设置
            tx_settings = {}
            if metadata is not None:
                tx_settings["metadata"] = metadata
            if timeout is not None:
                tx_settings["timeout"] = timeout
                
            # 调用原始函数,传入事务设置
            def wrapped_f(tx):
                if tx_settings:
                    for key, value in tx_settings.items():
                        setattr(tx, key, value)
                return f(tx)
                
            return wrapped_f
            
        return wrapper
    return decorator