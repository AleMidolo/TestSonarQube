import os
import platform

def _should_attempt_c_optimizations():
    """
    Devuelve un valor verdadero si deberíamos intentar usar las optimizaciones en C.

    Esto tiene en cuenta si estamos utilizando PyPy y el valor de la variable de entorno  
    ``PURE_PYTHON``, tal como se define en `_use_c_impl`.
    """
    # Verificar si estamos en PyPy
    is_pypy = platform.python_implementation() == "PyPy"
    
    # Verificar si la variable de entorno PURE_PYTHON está establecida
    pure_python = os.getenv("PURE_PYTHON", "").lower() in ("1", "true", "yes")
    
    # Intentar optimizaciones en C si no estamos en PyPy y no se ha forzado el uso de Python puro
    return not is_pypy and not pure_python