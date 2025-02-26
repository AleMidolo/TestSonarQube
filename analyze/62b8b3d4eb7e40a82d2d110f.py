import os
import sys

def _should_attempt_c_optimizations():
    """
    Devuelve un valor verdadero si deberíamos intentar usar las optimizaciones en C.

    Esto tiene en cuenta si estamos utilizando PyPy y el valor de la variable de entorno  
    ``PURE_PYTHON``, tal como se define en `_use_c_impl`.
    """
    is_pypy = 'pypy' in sys.version.lower()
    pure_python_env = os.getenv('PURE_PYTHON')

    return not is_pypy and (pure_python_env is None or pure_python_env.lower() != '1')