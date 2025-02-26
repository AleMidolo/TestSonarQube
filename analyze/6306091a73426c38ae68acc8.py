def list_of_file_names(settings_dirs, spec_option):
    """
    通过 `cli.ListOfFileNames()` 创建并返回一个新的 `IniType` 复合类型。
    创建一个新的 `IniType` 复合类型。
    """
    from cli import ListOfFileNames  # Assuming cli is a module that needs to be imported

    # Create a new IniType composite type using the ListOfFileNames function
    ini_type_instance = ListOfFileNames(settings_dirs, spec_option)
    
    return ini_type_instance