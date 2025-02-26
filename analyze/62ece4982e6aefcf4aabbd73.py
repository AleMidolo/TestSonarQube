import re
import sys

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
        platform = 1 if sys.platform in ['linux', 'darwin'] else 0

    if platform == 1:  # POSIX
        pattern = r'(?:"([^"]*)"|\'([^\']*)|(\S+))'
    else:  # Windows/CMD
        pattern = r'(?:"([^"]*)"|\'([^\']*)|([^"\s]+)?)'

    matches = re.findall(pattern, s)
    result = []
    for match in matches:
        result.append(next(filter(None, match)))  # Get the first non-empty match

    return result