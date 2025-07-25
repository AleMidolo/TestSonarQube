import os

def _should_attempt_c_optimizations():
    """
    如果我们使用 C 优化，则返回一个真值。

    如果我们应该尝试使用 C 优化，则返回一个真值。

    这会考虑我们是否运行在 PyPy 上，以及 `_use_c_impl` 中定义的 ``PURE_PYTHON`` 环境变量的值。
    """
    # 检查是否运行在 PyPy 上
    is_pypy = hasattr(sys, 'pypy_version_info')
    
    # 检查 PURE_PYTHON 环境变量的值
    pure_python = os.getenv('PURE_PYTHON', '').lower() in ('1', 'true', 'yes')
    
    # 如果不在 PyPy 上且 PURE_PYTHON 未设置为真值，则尝试 C 优化
    return not is_pypy and not pure_python