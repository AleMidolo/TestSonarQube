import os
import sys

def _should_attempt_c_optimizations():
    """
    यदि हमें C अनुकूलन का प्रयास करना चाहिए, तो एक सत्य मान लौटाएं।  

    यह इस बात को ध्यान में रखता है कि क्या हम PyPy पर हैं और `_use_c_impl` में परिभाषित ``PURE_PYTHON`` पर्यावरण चर का मान क्या है।
    """
    is_pypy = sys.platform.startswith('pypy')
    pure_python_env = os.getenv('_use_c_impl', 'False') == 'PURE_PYTHON'
    
    return is_pypy and not pure_python_env