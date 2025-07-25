def is_gitbash():
    """
    检查当前程序是否在 Windows 的 gitbash 终端中运行

    返回值:
      布尔值，如果是 gitbash 则返回真，否则返回假

    如果在 Windows 的 gitbash 中运行，则返回真
    :return: 如果是 gitbash 则返回真
    """
    import os
    import sys
    
    # 检查是否在Windows系统
    if os.name != 'nt':
        return False
        
    # 检查环境变量中是否包含MINGW或MSYS
    env_keys = os.environ.keys()
    git_env = any('MINGW' in key or 'MSYS' in key for key in env_keys)
    
    # 检查终端类型
    term = os.environ.get('TERM', '')
    is_term = 'xterm' in term.lower()
    
    # 如果同时满足环境变量和终端类型条件，则认为是在gitbash中
    return git_env and is_term