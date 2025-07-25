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
        platform = 1 if sys.platform != 'win32' else 0
    
    if platform == 1:  # POSIX style
        regex = re.compile(r'''((?:[^\s"']|"[^"]*"|'[^']*')+)''')
    else:  # Windows/CMD style
        regex = re.compile(r'''((?:[^\s"]|"[^"]*")+)''')
    
    return [match.group(0) for match in regex.finditer(s)]