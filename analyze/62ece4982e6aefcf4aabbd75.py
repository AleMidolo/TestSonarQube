def addignored(ignored):
    """
    使用 `git` 命令获取文件名，将其转换为列表，仅筛选被忽略的文件，对列表进行排序，并将这些文件作为一个字符串返回，文件名之间用逗号分隔。
    """
    import subprocess
    
    # 运行git ls-files命令获取所有文件
    result = subprocess.run(['git', 'ls-files', '--others', '--ignored', '--exclude-standard'], 
                          capture_output=True, 
                          text=True)
    
    # 将输出转换为列表并过滤空行
    files = [f for f in result.stdout.split('\n') if f]
    
    # 筛选被忽略的文件
    ignored_files = [f for f in files if f in ignored]
    
    # 对列表排序
    ignored_files.sort()
    
    # 用逗号连接文件名
    return ','.join(ignored_files)