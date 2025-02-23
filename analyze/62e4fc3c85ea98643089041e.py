def _inline_r_setup(code: str) -> str:
    """
    Some behaviour of R cannot be configured via env variables, but can
    only be configured via R options once R has started. These are set here.
    """
    import rpy2.robjects as ro

    # Set R options
    ro.r('options(stringsAsFactors = FALSE)')
    ro.r('options(scipen = 999)')  # Disable scientific notation
    ro.r('options(max.print = 1000)')  # Set max print output

    # Execute the provided R code
    ro.r(code)

    return "R setup complete and code executed."