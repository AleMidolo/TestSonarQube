def display(self, key, value):
    """
    打印和弦并播放旋律，格式如下：正常吉他演奏 -- 和弦: %s, 播放旋律: %s
    :param key:字符串, 和弦
    :param value:字符串, 播放旋律
    :return: str
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> context.display("C", "53231323")
    正常吉他演奏 -- 和弦: C, 播放旋律: 53231323

    """
    result = f"正常吉他演奏 -- 和弦: {key}, 播放旋律: {value}"
    print(result)
    return result