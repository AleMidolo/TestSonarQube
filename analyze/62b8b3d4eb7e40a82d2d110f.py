def _should_attempt_c_optimizations():
    """
    如果我们使用 C 优化，则返回一个真值。

    如果我们应该尝试使用 C 优化，则返回一个真值。

    这会考虑我们是否运行在 PyPy 上，以及 `_use_c_impl` 中定义的 ``PURE_PYTHON`` 环境变量的值。
    """
    import os
    return not (os.getenv('PURE_PYTHON') == '1' or 'pypy' in sys.version.lower())