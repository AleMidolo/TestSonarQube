def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Script para procesar argumentos de línea de comandos')
    
    # Agregar argumentos posicionales y opcionales
    parser.add_argument('--input', '-i', help='Archivo de entrada', required=False)
    parser.add_argument('--output', '-o', help='Archivo de salida', required=False)
    parser.add_argument('--verbose', '-v', action='store_true', help='Mostrar información detallada')
    
    # Si se pasan argumentos, usarlos. Si no, usar sys.argv[1:]
    if arguments:
        args = parser.parse_args(arguments)
    else:
        args = parser.parse_args()
        
    return args