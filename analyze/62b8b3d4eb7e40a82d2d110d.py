def _c_optimizations_required():
    """
    如果需要 C 优化，则返回一个真值。
    
    该函数使用了 `_use_c_impl` 中记录的 ``PURE_PYTHON`` 变量。
    """
    try:
        from ._use_c_impl import PURE_PYTHON
        return not PURE_PYTHON
    except ImportError:
        return False