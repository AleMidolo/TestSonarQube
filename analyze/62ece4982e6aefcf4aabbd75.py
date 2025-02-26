import subprocess

def addignored(ignored):
    """
    使用 `git` 命令获取文件名，将其转换为列表，仅筛选被忽略的文件，对列表进行排序，并将这些文件作为一个字符串返回，文件名之间用逗号分隔。
    """
    try:
        # 获取被忽略的文件列表
        result = subprocess.run(['git', 'ls-files', '--ignored', '--exclude-standard'], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                text=True, 
                                check=True)
        # 将结果转换为列表并去除空白字符
        ignored_files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        # 排序文件列表
        ignored_files.sort()
        # 将文件名用逗号连接成字符串
        return ','.join(ignored_files)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")
        return ""