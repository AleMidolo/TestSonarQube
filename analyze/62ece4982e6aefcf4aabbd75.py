def addignored(ignored):
    """
    使用 `git` 命令获取文件名，将其转换为列表，仅筛选被忽略的文件，对列表进行排序，并将这些文件作为一个字符串返回，文件名之间用逗号分隔。
    """
    import subprocess
    
    # 运行git命令获取被忽略的文件
    result = subprocess.run(['git', 'status', '--ignored', '--porcelain'], 
                          capture_output=True, 
                          text=True)
    
    # 将输出分割成行
    lines = result.stdout.split('\n')
    
    # 筛选出被忽略的文件 (以'!!'开头的行)
    ignored_files = []
    for line in lines:
        if line.startswith('!!'):
            # 去掉'!! '前缀并添加到列表
            ignored_files.append(line[3:])
            
    # 排序文件列表
    ignored_files.sort()
    
    # 将列表转换为逗号分隔的字符串
    return ','.join(ignored_files)