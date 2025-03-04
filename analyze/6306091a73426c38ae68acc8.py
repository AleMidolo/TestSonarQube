def list_of_file_names(settings_dirs, spec_option):
    """
    通过 `cli.ListOfFileNames()` 创建并返回一个新的 `IniType` 复合类型。
    创建一个新的 `IniType` 复合类型。
    """
    class ListOfFileNames:
        def __init__(self, settings_dirs, spec_option):
            self.settings_dirs = settings_dirs
            self.spec_option = spec_option
            self.file_names = []
            
        def get_file_names(self):
            """获取文件名列表"""
            for directory in self.settings_dirs:
                try:
                    # 获取目录下所有文件
                    files = os.listdir(directory)
                    # 根据spec_option过滤文件
                    if self.spec_option:
                        files = [f for f in files if f.endswith(self.spec_option)]
                    self.file_names.extend(files)
                except OSError:
                    continue
            return self.file_names
            
        def __str__(self):
            return str(self.get_file_names())
            
    return ListOfFileNames(settings_dirs, spec_option)