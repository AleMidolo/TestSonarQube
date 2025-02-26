def _inline_r_setup(code: str) -> str:
    """
    Alcuni comportamenti di R non possono essere configurati tramite variabili di ambiente, ma possono essere configurati solo tramite opzioni di R una volta che R è stato avviato. Questi vengono impostati qui.
    """
    import rpy2.robjects as ro

    # Set R options
    ro.r('options(stringsAsFactors = FALSE)')
    ro.r('options(scipen = 999)')  # Disable scientific notation
    ro.r('options(max.print = 1000)')  # Set maximum number of printed items

    # Execute the provided R code
    ro.r(code)

    return "R setup complete and code executed."