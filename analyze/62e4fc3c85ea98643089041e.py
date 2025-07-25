def _inline_r_setup(code: str) -> str:
    """
    Algunos comportamientos de R no pueden configurarse mediante variables de entorno, sino que solo pueden configurarse a través de opciones de R una vez que R ha iniciado. Estas se configuran aquí.
    """
    r_setup_code = """
    options(
        repos = c(CRAN = "https://cloud.r-project.org/"),
        warn = 1,
        stringsAsFactors = FALSE
    )
    """
    return f"{r_setup_code}\n{code}"