def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None, db=None, imp_user=None, dehydration_hooks=None, hydration_hooks=None, **handlers):
    """
    :param mode: 路由的访问模式 - "READ" 或 "WRITE"（默认值）
    :param bookmarks: 该事务应从这些书签（bookmark）值之后开始执行的可迭代对象
    :param metadata: 附加到事务的自定义元数据字典
    :param timeout: 事务执行的超时时间（以秒为单位）
    :param db: 要开始事务的数据库名称
      需要 Bolt 4.0+。
    :param imp_user: 要模拟的用户
      需要 Bolt 4.4+。
    :param dehydration_hooks: 用于处理类型dehydration的钩子（字典，键为类型（类），值为dehydration函数）。dehydration函数接收一个值，并返回一个 PackStream 可识别的对象。
    :param hydration_hooks: 用于处理类型hydration的钩子（映射，键为类型（类），值为hydration函数）。hydration函数接收一个 PackStream 可识别的值，并可以返回任意对象。
    :param handlers: 传递给返回的Response对象的处理函数
    :return: Response 对象
    """
    # 初始化事务配置
    config = {
        "mode": mode,
        "bookmarks": bookmarks,
        "metadata": metadata,
        "timeout": timeout,
        "db": db,
        "imp_user": imp_user,
        "dehydration_hooks": dehydration_hooks,
        "hydration_hooks": hydration_hooks,
    }
    
    # 过滤掉None值
    config = {k: v for k, v in config.items() if v is not None}
    
    # 合并handlers
    config.update(handlers)
    
    # 创建并返回Response对象
    return Response(config)