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
        platform = 1 if sys.platform != 'win32' else 0
    
    if platform == 1:  # POSIX
        pattern = re.compile(r"""((?:[^\s"']|"[^"]*"|'[^']*')+)""")
    elif platform == 0:  # Windows/CMD
        pattern = re.compile(r"""((?:[^\s"]|"[^"]*")+)""")
    else:
        raise ValueError("Invalid platform value. Use 'this', 1 (POSIX), or 0 (Windows/CMD).")
    
    return pattern.findall(s)