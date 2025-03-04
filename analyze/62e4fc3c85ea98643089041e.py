def _inline_r_setup(code: str) -> str:
    """
    一些 R 的行为无法通过环境变量进行配置，
    只能在 R 启动后通过 R 的选项进行配置。这些选项在此处设置。
    """
    setup_code = """
    options(warn=-1)  # Suppress warnings
    options(width=10000)  # Prevent line wrapping in output
    options(encoding='UTF-8')  # Set encoding to UTF-8
    """
    
    # Combine setup code with input code
    full_code = setup_code + "\n" + code
    
    return full_code