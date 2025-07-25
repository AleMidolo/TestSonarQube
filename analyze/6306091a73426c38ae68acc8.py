def list_of_file_names(settings_dirs, spec_option):
    """
    通过 `cli.ListOfFileNames()` 创建并返回一个新的 `IniType` 复合类型。
    创建一个新的 `IniType` 复合类型。
    """
    class ListOfFileNames:
        def __init__(self):
            self.settings_dirs = settings_dirs
            self.spec_option = spec_option
            self.file_names = []

        def get_file_names(self):
            """获取文件名列表"""
            import os
            for directory in self.settings_dirs:
                if os.path.exists(directory):
                    for file in os.listdir(directory):
                        if file.endswith(self.spec_option):
                            self.file_names.append(os.path.join(directory, file))
            return self.file_names

    ini_type = ListOfFileNames()
    return ini_type.get_file_names()