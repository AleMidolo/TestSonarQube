import os

def _c_optimizations_ignored():
    """
    如果获取到的环境变量 "PURE_PYTHON" 不是 None 且不等于 0，则返回真，否则返回假。
    与 `_c_optimizations_required` 功能相反。
    """
    return os.getenv("PURE_PYTHON") is not None and os.getenv("PURE_PYTHON") != '0'