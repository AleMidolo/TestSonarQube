def _c_optimizations_required():
    try:
        from . import PURE_PYTHON
        return not PURE_PYTHON
    except ImportError:
        return True