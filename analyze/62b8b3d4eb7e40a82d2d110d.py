def _c_optimizations_required():
    try:
        from ._use_c_impl import PURE_PYTHON
        return not PURE_PYTHON
    except ImportError:
        return True