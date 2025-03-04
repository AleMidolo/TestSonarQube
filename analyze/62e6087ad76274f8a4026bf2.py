def discard(self, n=-1, qid=-1, dehydration_hooks=None, hydration_hooks=None, **handlers):
    """
    将一个DISCARD消息添加到输出队列。

    :param n: 要丢弃的记录数量，默认值为 -1（全部丢弃）
    :param qid: 要丢弃的查询ID，默认值为 -1（最后一个查询）
    :param dehydration_hooks: 用于处理类型dehydration的钩子（字典，键为类型（类），值为dehydration函数）。dehydration函数接收一个值，并返回一个 PackStream 可识别的对象。
    :param hydration_hooks: 用于处理类型hydration的钩子（映射，键为类型（类），值为hydration函数）。hydration函数接收一个 PackStream 可识别的值，并可以返回任意对象。
    :param handlers: 传递给返回的Response对象的处理函数
    """
    # 创建消息参数字典
    message_params = {
        "n": n,
        "qid": qid
    }

    # 创建消息结构
    message = {
        "signature": 0x2F,  # DISCARD message signature
        "fields": message_params
    }
    
    # 应用dehydration hooks（如果有）
    if dehydration_hooks:
        for type_, hook in dehydration_hooks.items():
            if isinstance(message_params, type_):
                message_params = hook(message_params)
    
    # 将消息添加到输出队列
    self._append(message)
    
    # 创建响应对象
    response = Response(
        hydration_hooks=hydration_hooks,
        **handlers
    )
    
    return response