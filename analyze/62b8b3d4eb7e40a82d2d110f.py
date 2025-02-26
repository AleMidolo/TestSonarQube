import os
import sys

def _should_attempt_c_optimizations():
    """
    Devuelve un valor verdadero si deberíamos intentar usar las optimizaciones en C.

    Esto tiene en cuenta si estamos utilizando PyPy y el valor de la variable de entorno  
    ``PURE_PYTHON``, tal como se define en `_use_c_impl`.
    """
    is_pypy = 'pypy' in sys.version.lower()
    pure_python = os.getenv('PURE_PYTHON', '0') == '1'
    
    return not is_pypy and not pure_python