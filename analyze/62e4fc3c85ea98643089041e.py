def _inline_r_setup(code: str) -> str:
    """
    Algunos comportamientos de R no pueden configurarse mediante variables de entorno, sino que solo pueden configurarse a través de opciones de R una vez que R ha iniciado. Estas se configuran aquí.
    """
    # Aquí se pueden establecer opciones de R necesarias para la ejecución del código
    options = [
        "options(stringsAsFactors = FALSE)",  # Ejemplo de opción
        "options(scipen = 999)"                # Evitar notación científica
    ]
    
    # Unir las opciones en un solo bloque de código
    setup_code = "\n".join(options)
    
    # Devolver el código de configuración junto con el código proporcionado
    return f"{setup_code}\n{code}"