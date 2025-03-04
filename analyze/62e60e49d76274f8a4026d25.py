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
            def run_tx(tx):
                # 如果有元数据,设置到事务中
                if metadata:
                    tx.set_metadata(metadata)
                # 如果有超时设置,应用到事务中    
                if timeout is not None:
                    tx.set_timeout(timeout)
                # 执行实际的事务函数    
                return f(tx, *args, **kwargs)
                
            return run_tx
            
        return wrapper
    return decorator