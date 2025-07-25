def is_gitbash():
    """
    检查当前程序是否在 Windows 的 gitbash 终端中运行

    返回值:
      布尔值，如果是 gitbash 则返回真，否则返回假

    如果在 Windows 的 gitbash 中运行，则返回真
    :return: 如果是 gitbash 则返回真
    """
    import os
    return 'MINGW' in os.environ.get('TERM', '') or 'gitbash' in os.environ.get('SHELL', '')