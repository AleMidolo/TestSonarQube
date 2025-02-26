def _inline_r_setup(code: str) -> str:
    """
    Algunos comportamientos de R no pueden configurarse mediante variables de entorno, sino que solo pueden configurarse a través de opciones de R una vez que R ha iniciado. Estas se configuran aquí.
    """
    import rpy2.robjects as ro

    # Configurar opciones de R
    ro.r('options(stringsAsFactors = FALSE)')
    ro.r('options(scipen = 999)')  # Evitar notación científica
    ro.r('options(max.print = 1000)')  # Limitar la cantidad de impresión

    # Ejecutar el código R proporcionado
    ro.r(code)

    return "Configuración de R completada y código ejecutado."