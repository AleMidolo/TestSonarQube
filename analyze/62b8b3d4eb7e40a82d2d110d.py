def _c_optimizations_required():
    import os
    
    pure_python = os.environ.get('PURE_PYTHON', '').lower()
    
    # Return True if C optimizations are required (PURE_PYTHON is not set to true/1)
    return not pure_python in ('true', '1')