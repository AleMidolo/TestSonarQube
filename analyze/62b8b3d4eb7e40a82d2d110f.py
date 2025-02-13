import os
import sys

def _should_attempt_c_optimizations():
    if 'PURE_PYTHON' in os.environ:
        return False
    if sys.platform == 'pypy':
        return True
    return True