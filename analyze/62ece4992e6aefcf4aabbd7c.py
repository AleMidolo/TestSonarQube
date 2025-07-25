def oneline(script, separator=" && "):
    """
    将脚本转换为带有给定分隔符的单行命令。
    参数：
      `script`: str  
      `separator`: str  
    返回值：
      `str`，单行命令。

    将脚本转换为单行命令。
    这在通过 SSH 执行单行脚本时非常有用。

    :param script:
    :return:
    """
    return separator.join(line.strip() for line in script.strip().splitlines() if line.strip())