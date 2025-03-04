def get_config():
    """
    返回一个新的 `VersioneerConfig()` 对象，并设置其各种属性。
    创建、填充并返回 `VersioneerConfig()` 对象。
    """
    class VersioneerConfig:
        def __init__(self):
            self.VCS = 'git'  # 版本控制系统
            self.style = 'pep440'  # 版本号风格
            self.tag_prefix = ''  # 标签前缀
            self.parentdir_prefix = ''  # 父目录前缀
            self.versionfile_source = ''  # 版本文件源
            self.verbose = False  # 是否详细输出
            self.update_files = True  # 是否更新文件
            self.tag_missing_error = True  # 缺少标签时是否报错
            self.lookupfile = None  # 查找文件
            self.root = '.'  # 根目录
            self.versionfile_build = None  # 构建版本文件
            self.parentdir_glob_pattern = '*-*'  # 父目录匹配模式
            self.git_describe_command = None  # git describe 命令
            self.scan_subdirs = False  # 是否扫描子目录

    cfg = VersioneerConfig()
    return cfg