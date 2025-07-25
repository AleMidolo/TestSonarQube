def _c_optimizations_available():
    try:
        from . import _speedups
        return _speedups
    except ImportError:
        return False