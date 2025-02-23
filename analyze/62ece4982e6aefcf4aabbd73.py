import re
import platform as sys_platform

def split(s, platform='this'):
    """
    Variante multiplataforma de `shlex.split()` para dividir cadenas de línea de comandos.  
    Diseñado para su uso con `subprocess`, inyección de argumentos (`argv`), etc. Utiliza expresiones regulares rápidas.

    platform:  'this'= detección automática de la plataforma actual;  
      1= POSIX;  
      0=Windows/CMD  
      (otros valores están reservados).
    """
    if platform == 'this':
        platform = 1 if sys_platform.system() != 'Windows' else 0

    if platform == 1:  # POSIX
        pattern = r'(?:"([^"]*)"|\'([^\']*)|(\S+)|\s+)'
    elif platform == 0:  # Windows
        pattern = r'(?:"([^"]*)"|\'([^\']*)|([^"\s]+)|\s+)'
    else:
        raise ValueError("Unsupported platform value")

    tokens = []
    for match in re.finditer(pattern, s):
        token = match.group(1) or match.group(2) or match.group(3)
        if token is not None:
            tokens.append(token)

    return tokens