def _inline_r_setup(code: str) -> str:
    """
    Some behaviour of R cannot be configured via env variables, but can
    only be configured via R options once R has started. These are set here.
    """
    setup_code = """
    options(
        repos = c(CRAN = "https://cloud.r-project.org/"),
        warn = 1,
        stringsAsFactors = FALSE,
        encoding = "UTF-8"
    )
    """
    return f"{setup_code}\n{code}"