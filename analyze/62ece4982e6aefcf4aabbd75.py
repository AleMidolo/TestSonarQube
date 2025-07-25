def addignored(ignored):
    """
    使用 `git` 命令获取文件名，将其转换为列表，仅筛选被忽略的文件，对列表进行排序，并将这些文件作为一个字符串返回，文件名之间用逗号分隔。
    """
    import subprocess
    
    # 运行git命令获取被忽略的文件列表
    try:
        # 使用git ls-files --others --ignored --exclude-standard命令获取被忽略的文件
        result = subprocess.run(['git', 'ls-files', '--others', '--ignored', '--exclude-standard'], 
                              capture_output=True, 
                              text=True)
        
        # 将输出按行分割成列表
        files = result.stdout.strip().split('\n')
        
        # 过滤空字符串并排序
        files = sorted([f for f in files if f])
        
        # 将文件列表用逗号连接成字符串
        return ','.join(files)
        
    except subprocess.CalledProcessError:
        # 如果git命令执行失败，返回空字符串
        return ''