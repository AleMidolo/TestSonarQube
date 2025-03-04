def _c_optimizations_required():
    """
    Return a true value if the C optimizations are required.

    This uses the ``PURE_PYTHON`` variable as documented in `_use_c_impl`.
    """
    import os
    
    pure_python = os.environ.get('PURE_PYTHON', '').lower()
    
    # Return True if C optimizations are required (PURE_PYTHON is not set to true/1)
    return not pure_python in ('true', '1', 't', 'y', 'yes')