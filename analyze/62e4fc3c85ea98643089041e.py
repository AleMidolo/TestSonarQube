def _inline_r_setup(code: str) -> str:
    """
    一些 R 的行为无法通过环境变量进行配置，
    只能在 R 启动后通过 R 的选项进行配置。这些选项在此处设置。
    """
    import rpy2.robjects as ro

    # Set R options
    ro.r('options(stringsAsFactors = FALSE)')
    ro.r('options(scipen = 999)')  # Disable scientific notation
    ro.r('options(max.print = 1000)')  # Set max print limit

    # Execute the provided R code
    ro.r(code)

    return "R setup complete and code executed."