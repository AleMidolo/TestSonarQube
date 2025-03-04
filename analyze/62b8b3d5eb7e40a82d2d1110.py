def _c_optimizations_available():
    """
    如果可用，则返回 C 优化模块，否则返回一个假值。

    如果需要优化模块但不可用，则会引发 `ImportError` 异常。 

    此函数并不决定是否应该使用这些优化模块。
    """
    try:
        import _speedups
        return _speedups
    except ImportError:
        return False