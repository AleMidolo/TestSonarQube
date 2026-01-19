def generate_primes(self):
    """
    使用钱德拉塞卡筛法生成指定限制内的素数。
    :return: list, 一个素数列表
    >>> cs = ChandrasekharSieve(20)
    >>> cs.generate_primes()
    [2, 3, 5, 7, 11, 13, 17, 19]

    """
    if self.limit < 2:
        return []
    
    # 创建布尔数组，初始化所有数为True（假设都是素数）
    is_prime = [True] * (self.limit + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是素数
    
    # 埃拉托斯特尼筛法（钱德拉塞卡筛法是其变体）
    p = 2
    while p * p <= self.limit:
        if is_prime[p]:
            # 标记p的所有倍数为非素数
            for i in range(p * p, self.limit + 1, p):
                is_prime[i] = False
        p += 1
    
    # 收集所有素数
    primes = [num for num in range(2, self.limit + 1) if is_prime[num]]
    return primes