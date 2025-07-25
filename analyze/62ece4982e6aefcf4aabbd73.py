def split(s, platform='this'):
    import re
    import os
    import sys

    # Determinar plataforma
    if platform == 'this':
        platform = 1 if os.name == 'posix' else 0
    
    if platform == 1:  # POSIX
        # Patrón para dividir argumentos estilo POSIX/bash
        pattern = r'''((?:[^ "']\S*|"[^"]*"|'[^']*')+)'''
    else:  # Windows/CMD
        # Patrón para dividir argumentos estilo Windows CMD 
        pattern = r'''((?:[^ "]\S*|"[^"]*")+)'''
    
    # Dividir la cadena usando el patrón apropiado
    args = re.findall(pattern, s)
    
    # Procesar cada argumento
    processed_args = []
    for arg in args:
        # Eliminar comillas externas si existen
        if (arg.startswith('"') and arg.endswith('"')) or \
           (arg.startswith("'") and arg.endswith("'")):
            arg = arg[1:-1]
        processed_args.append(arg)
        
    return processed_args