from collections import defaultdict
from functools import wraps

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        # 存储缓存结果
        cache = {}
        # 存储每个key的使用频率
        frequencies = defaultdict(int)
        # 存储每个频率对应的key集合
        freq_keys = defaultdict(set)
        # 记录最小频率
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
                freq_keys[old_freq].remove(key)
                if not freq_keys[old_freq] and old_freq == min_freq:
                    min_freq += 1
                freq_keys[frequencies[key]].add(key)
                return cache[key]

            # 如果缓存已满,删除使用频率最低的项
            if len(cache) >= maxsize:
                # 获取最低频率对应的任意一个key
                lfu_key = next(iter(freq_keys[min_freq]))
                # 删除该key的所有相关信息
                cache.pop(lfu_key)
                freq_keys[min_freq].remove(lfu_key)
                frequencies.pop(lfu_key)

            # 计算新值并加入缓存
            result = func(*args, **kwargs)
            cache[key] = result
            frequencies[key] = 1
            freq_keys[1].add(key)
            min_freq = 1
            return result

        # 添加缓存清理方法
        def clear_cache():
            cache.clear()
            frequencies.clear()
            freq_keys.clear()
            nonlocal min_freq
            min_freq = 0

        wrapper.clear_cache = clear_cache
        return wrapper

    return decorator