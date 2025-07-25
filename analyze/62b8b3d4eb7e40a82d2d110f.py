import os
import platform

def _should_attempt_c_optimizations():
    """
    如果我们使用 C 优化，则返回一个真值。

    如果我们应该尝试使用 C 优化，则返回一个真值。

    这会考虑我们是否运行在 PyPy 上，以及 `_use_c_impl` 中定义的 ``PURE_PYTHON`` 环境变量的值。
    """
    # Check if running on PyPy
    is_pypy = platform.python_implementation() == "PyPy"
    
    # Check if PURE_PYTHON environment variable is set
    pure_python = os.getenv("PURE_PYTHON", "").lower() in ("1", "true", "yes")
    
    # Return True if not running on PyPy and PURE_PYTHON is not set
    return not is_pypy and not pure_python