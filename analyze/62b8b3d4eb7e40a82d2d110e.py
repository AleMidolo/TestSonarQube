import os

def _c_optimizations_ignored():
    return os.environ.get("PURE_PYTHON") not in [None, '0']