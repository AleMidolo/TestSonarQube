def list_of_file_names(settings_dirs, spec_option):
    """
    通过 `cli.ListOfFileNames()` 创建并返回一个新的 `IniType` 复合类型。
    创建一个新的 `IniType` 复合类型。
    """
    class ListOfFileNames:
        def __init__(self, settings_dirs, spec_option):
            self.settings_dirs = settings_dirs
            self.spec_option = spec_option
            self.files = []
            
        def get_files(self):
            """获取文件列表"""
            import os
            for directory in self.settings_dirs:
                if os.path.exists(directory):
                    for file in os.listdir(directory):
                        if file.endswith(self.spec_option):
                            self.files.append(os.path.join(directory, file))
            return self.files
            
        def __str__(self):
            return str(self.get_files())
            
    return ListOfFileNames(settings_dirs, spec_option)