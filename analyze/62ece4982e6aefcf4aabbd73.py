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
        pattern = re.compile(r"""
            (?:[^\s"']+|"[^"]*"|'[^']*')+
        """, re.VERBOSE)
    else:  # Windows/CMD style
        pattern = re.compile(r"""
            (?:[^\s"]+|"[^"]*")+
        """, re.VERBOSE)
    
    matches = pattern.findall(s)
    return [match.strip('"\'') for match in matches]