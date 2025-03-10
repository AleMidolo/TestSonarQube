import os

def _should_attempt_c_optimizations():
    """
    Devuelve un valor verdadero si deberíamos intentar usar las optimizaciones en C.

    Esto tiene en cuenta si estamos utilizando PyPy y el valor de la variable de entorno  
    ``PURE_PYTHON``, tal como se define en `_use_c_impl`.
    """
    # Verificar si estamos en PyPy
    is_pypy = hasattr(sys, 'pypy_version_info')
    
    # Verificar la variable de entorno PURE_PYTHON
    pure_python = os.getenv('PURE_PYTHON', '').lower() in ('1', 'true', 'yes')
    
    # Intentar optimizaciones en C si no estamos en PyPy y PURE_PYTHON no está activado
    return not is_pypy and not pure_python