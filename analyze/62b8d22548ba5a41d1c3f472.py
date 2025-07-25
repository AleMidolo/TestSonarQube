def cachedmethod(cache, key=hashkey, lock=None):
    """
    返回一个装饰器函数，可以调用缓存中的结果。
    该装饰器用于包装类方法或实例方法，使其成为一个具备记忆功能的可调用对象，并将结果存储在缓存中。
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # 生成缓存键
            k = key(self, *args, **kwargs)
            
            # 如果指定了锁,则获取锁
            if lock is not None:
                lock.acquire()
                
            try:
                # 尝试从缓存中获取结果
                try:
                    return cache[k]
                except KeyError:
                    pass
                
                # 如果缓存中没有,则调用原方法计算结果
                result = method(self, *args, **kwargs)
                
                # 将结果存入缓存
                try:
                    cache[k] = result
                except TypeError:
                    pass
                
                return result
                
            finally:
                # 如果获取了锁,则释放锁
                if lock is not None:
                    lock.release()
                    
        # 保留原方法的文档字符串
        wrapper.__doc__ = method.__doc__
        return wrapper
        
    return decorator