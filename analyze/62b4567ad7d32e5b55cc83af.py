def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Script para procesar argumentos de línea de comandos')
    
    # Si no se pasan argumentos, usar sys.argv[1:]
    if not arguments:
        import sys
        arguments = sys.argv[1:]
    
    # Agregar argumentos esperados
    parser.add_argument('-i', '--input', help='Archivo de entrada', required=False)
    parser.add_argument('-o', '--output', help='Archivo de salida', required=False)
    parser.add_argument('-v', '--verbose', help='Mostrar información detallada', action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    
    # Parsear los argumentos
    args = parser.parse_args(arguments)
    
    return args