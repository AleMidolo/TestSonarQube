def _inline_r_setup(code: str) -> str:
    """
    Alcuni comportamenti di R non possono essere configurati tramite variabili di ambiente, ma possono essere configurati solo tramite opzioni di R una volta che R è stato avviato. Questi vengono impostati qui.
    """
    import rpy2.robjects as ro

    # Imposta le opzioni di R
    ro.r('options(stringsAsFactors = FALSE)')
    ro.r('options(scipen = 999)')  # Disabilita la notazione scientifica
    ro.r('options(max.print = 1000)')  # Limita il numero di righe stampate

    # Esegui il codice R fornito
    ro.r(code)

    return "R setup complete and code executed."