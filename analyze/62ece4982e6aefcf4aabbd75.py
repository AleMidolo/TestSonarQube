import subprocess

def addignored(ignored):
    """
    使用 `git` 命令获取文件名，将其转换为列表，仅筛选被忽略的文件，对列表进行排序，并将这些文件作为一个字符串返回，文件名之间用逗号分隔。
    """
    # 使用 git ls-files 命令获取所有文件
    result = subprocess.run(['git', 'ls-files', '--others', '--ignored', '--exclude-standard'], stdout=subprocess.PIPE)
    files = result.stdout.decode('utf-8').splitlines()
    
    # 筛选被忽略的文件
    ignored_files = [file for file in files if file in ignored]
    
    # 对列表进行排序
    ignored_files.sort()
    
    # 将文件名用逗号分隔并返回
    return ', '.join(ignored_files)