def _inline_r_setup(code: str) -> str:
    """
    一些 R 的行为无法通过环境变量进行配置，
    只能在 R 启动后通过 R 的选项进行配置。这些选项在此处设置。
    """
    setup_code = """
    options(
        repos = c(CRAN = "https://cloud.r-project.org"),
        warn = 1,
        stringsAsFactors = FALSE
    )
    """
    return f"{setup_code}\n{code}"