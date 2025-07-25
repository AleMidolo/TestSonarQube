def addignored(ignored):
    """
    使用 `git` 命令获取文件名，将其转换为列表，仅筛选被忽略的文件，对列表进行排序，并将这些文件作为一个字符串返回，文件名之间用逗号分隔。
    """
    import subprocess
    
    # 运行git命令获取被忽略的文件列表
    try:
        result = subprocess.run(['git', 'status', '--ignored', '--porcelain'], 
                              capture_output=True, 
                              text=True)
        output = result.stdout
    except subprocess.CalledProcessError:
        return ""
        
    # 将输出转换为列表并筛选被忽略的文件
    ignored_files = []
    for line in output.split('\n'):
        if line.startswith('!!'):  # git status中被忽略的文件以!!开头
            filename = line[3:].strip()  # 去掉!!和空格
            ignored_files.append(filename)
            
    # 排序并用逗号连接
    ignored_files.sort()
    return ','.join(ignored_files)