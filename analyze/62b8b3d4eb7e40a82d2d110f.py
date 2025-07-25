def _should_attempt_c_optimizations():
    """
    如果我们使用 C 优化，则返回一个真值。

    如果我们应该尝试使用 C 优化，则返回一个真值。

    这会考虑我们是否运行在 PyPy 上，以及 `_use_c_impl` 中定义的 ``PURE_PYTHON`` 环境变量的值。
    """
    import os
    import platform

    # Check if running on PyPy
    is_pypy = platform.python_implementation() == 'PyPy'

    # Check PURE_PYTHON environment variable
    pure_python = os.environ.get('PURE_PYTHON', '').lower()
    use_pure_python = pure_python in ('1', 'true', 'yes', 'on')

    # Return True if we should use C optimizations:
    # - Not running on PyPy
    # - PURE_PYTHON is not set to a truthy value
    return not (is_pypy or use_pure_python)