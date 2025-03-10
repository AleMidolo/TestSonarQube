def _inline_r_setup(code: str) -> str:
    """
    Algunos comportamientos de R no pueden configurarse mediante variables de entorno, sino que solo pueden configurarse a través de opciones de R una vez que R ha iniciado. Estas se configuran aquí.
    """
    setup_code = """
    options(repos = c(CRAN = "https://cloud.r-project.org/"))
    options(warn = 1)
    options(stringsAsFactors = FALSE)
    """
    return f"{setup_code}\n{code}"