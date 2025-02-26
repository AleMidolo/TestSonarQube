def _should_attempt_c_optimizations():
    """
    Devuelve un valor verdadero si deberíamos intentar usar las optimizaciones en C.

    Esto tiene en cuenta si estamos utilizando PyPy y el valor de la variable de entorno  
    ``PURE_PYTHON``, tal como se define en `_use_c_impl`.
    """
    import os
    import sys

    # Check if we are using PyPy
    is_pypy = 'pypy' in sys.version.lower()

    # Check the environment variable PURE_PYTHON
    pure_python = os.getenv('PURE_PYTHON', '0') == '1'

    # Return True if we are not using PyPy and PURE_PYTHON is not set
    return not is_pypy and not pure_python