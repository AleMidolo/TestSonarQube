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
            def run_tx(tx):
                # 如果有metadata,设置事务元数据
                if metadata:
                    tx.set_metadata(metadata)
                # 如果有timeout,设置事务超时
                if timeout is not None:
                    tx.set_timeout(timeout)
                # 执行原始事务函数    
                return f(tx, *args, **kwargs)
                
            return run_tx
            
        return wrapper
    return decorator