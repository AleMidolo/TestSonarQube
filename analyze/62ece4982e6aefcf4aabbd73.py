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
        pattern = r'(?:"([^"]*)"|\'([^\']*)|(\S+))'
    elif platform == 0:  # Windows
        pattern = r'(?:"([^"]*)"|\'([^\']*)|([^"\s]+)?)'
    else:
        raise ValueError("Unsupported platform value")

    matches = re.findall(pattern, s)
    return [m[0] or m[1] or m[2] for m in matches]