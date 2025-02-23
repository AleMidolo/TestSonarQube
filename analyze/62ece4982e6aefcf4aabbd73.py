import re
import sys

def split(s, platform='this'):
    """
    ### Variante multi-piattaforma di `shlex.split()` per la divisione di stringhe da riga di comando.  
    Progettata per l'uso con `subprocess`, per l'iniezione di argomenti (`argv`) ecc. Utilizza espressioni regolari (REGEX) veloci.

    - **platform**:  
      - `'this'`: rilevamento automatico della piattaforma corrente.  
      - `1`: stile POSIX.  
      - `0`: stile Windows/CMD.  
      - (altri valori riservati).
    """
    if platform == 'this':
        platform = 1 if sys.platform.startswith('linux') or sys.platform == 'darwin' else 0

    if platform == 1:  # POSIX
        pattern = r'(?:"([^"]*)"|\'([^\']*)|(\S+))'
    else:  # Windows/CMD
        pattern = r'(?:"([^"]*)"|\'([^\']*)|([^"\s]+))'

    matches = re.findall(pattern, s)
    return [m[0] or m[1] or m[2] for m in matches]