def _inline_r_setup(code: str) -> str:
    """
    Alcuni comportamenti di R non possono essere configurati tramite variabili di ambiente, ma possono essere configurati solo tramite opzioni di R una volta che R è stato avviato. Questi vengono impostati qui.
    """
    setup_code = """
    options(
        repos = c(CRAN = "https://cloud.r-project.org/"),
        warn = 1,
        stringsAsFactors = FALSE
    )
    """
    return f"{setup_code}\n{code}"