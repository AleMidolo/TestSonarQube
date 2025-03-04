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
    for key in ['MINGW_PREFIX', 'MSYSTEM']:
        if key in env_keys:
            return True
            
    # 检查终端程序名称
    if sys.stdout.isatty():
        term = os.environ.get('TERM')
        if term and ('mingw' in term.lower() or 'msys' in term.lower()):
            return True
            
    return False