import subprocess

def addignored(ignored):
    """
    使用 `git` 命令获取文件名，将其转换为列表，仅筛选被忽略的文件，对列表进行排序，并将这些文件作为一个字符串返回，文件名之间用逗号分隔。
    """
    # 使用 git ls-files 命令获取所有文件
    result = subprocess.run(['git', 'ls-files', '--others', '--ignored', '--exclude-standard'], 
                            stdout=subprocess.PIPE, text=True)
    
    # 将输出转换为文件列表
    files = result.stdout.splitlines()
    
    # 筛选被忽略的文件
    ignored_files = [file for file in files if file in ignored]
    
    # 对列表进行排序
    ignored_files.sort()
    
    # 将文件列表转换为逗号分隔的字符串
    return ', '.join(ignored_files)