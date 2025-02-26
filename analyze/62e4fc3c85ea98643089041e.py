def _inline_r_setup(code: str) -> str:
    """
    一些 R 的行为无法通过环境变量进行配置，
    只能在 R 启动后通过 R 的选项进行配置。这些选项在此处设置。
    """
    # 这里可以设置一些 R 的选项
    options = {
        "stringsAsFactors": False,
        "warn": -1,
        "max.print": 1000
    }
    
    # 生成 R 代码来设置这些选项
    setup_code = "\n".join(f"options({key} = {value})" for key, value in options.items())
    
    # 返回设置选项的 R 代码
    return f"{setup_code}\n{code}"