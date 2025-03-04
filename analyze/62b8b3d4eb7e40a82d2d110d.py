def _c_optimizations_required():
    import os
    
    pure_python = os.environ.get('PURE_PYTHON', '0').lower()
    
    # Return True if C optimizations are required (PURE_PYTHON is falsy)
    return pure_python not in ('1', 'true', 'yes', 'on')