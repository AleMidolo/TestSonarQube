from collections import defaultdict
from functools import wraps

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        # 存储缓存结果
        cache = {}
        # 存储每个key的使用频率
        frequencies = defaultdict(int)
        # 存储每个频率对应的keys
        freq_list = defaultdict(set)
        # 当前最小频率
        min_freq = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 根据typed参数决定是否区分参数类型
            if typed:
                key = (*args, *sorted(kwargs.items()), 
                      *(type(arg) for arg in args),
                      *(type(v) for k, v in sorted(kwargs.items())))
            else:
                key = (*args, *sorted(kwargs.items()))
                
            # 如果key在缓存中
            if key in cache:
                # 更新使用频率
                old_freq = frequencies[key]
                frequencies[key] += 1
                freq_list[old_freq].remove(key)
                if not freq_list[old_freq] and old_freq == min_freq:
                    min_freq += 1
                freq_list[frequencies[key]].add(key)
                return cache[key]
            
            # 计算新结果
            result = func(*args, **kwargs)
            
            # 如果缓存已满,删除使用频率最少的项
            if len(cache) >= maxsize:
                # 获取最小频率对应的任意一个key
                lfu_key = next(iter(freq_list[min_freq]))
                # 删除该key的所有相关信息
                cache.pop(lfu_key)
                freq_list[min_freq].remove(lfu_key)
                del frequencies[lfu_key]
            
            # 添加新结果到缓存
            cache[key] = result
            frequencies[key] = 1
            freq_list[1].add(key)
            min_freq = 1
            
            return result
            
        # 添加缓存清理方法
        def clear_cache():
            cache.clear()
            frequencies.clear()
            freq_list.clear()
            nonlocal min_freq
            min_freq = 0
            
        wrapper.clear_cache = clear_cache
        return wrapper
        
    return decorator