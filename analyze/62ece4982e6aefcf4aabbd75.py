def addignored(ignored):
    """
    使用 `git` 命令获取文件名，将其转换为列表，仅筛选被忽略的文件，对列表进行排序，并将这些文件作为一个字符串返回，文件名之间用逗号分隔。
    """
    import subprocess

    # 获取被忽略的文件列表
    result = subprocess.run(['git', 'ls-files', '--ignored', '--exclude-standard'], 
                            stdout=subprocess.PIPE, 
                            text=True)
    
    # 将结果转换为列表并去除空白字符
    ignored_files = result.stdout.strip().split('\n')
    
    # 排序文件列表
    ignored_files.sort()
    
    # 将文件名用逗号连接成字符串
    return ','.join(ignored_files)