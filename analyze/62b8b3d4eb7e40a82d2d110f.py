import os
import sys

def _should_attempt_c_optimizations():
    """
    यदि हमें C अनुकूलन का प्रयास करना चाहिए, तो एक सत्य मान लौटाएं।  

    यह इस बात को ध्यान में रखता है कि क्या हम PyPy पर हैं और `_use_c_impl` में परिभाषित ``PURE_PYTHON`` पर्यावरण चर का मान क्या है।
    """
    pure_python_env = os.getenv('_use_c_impl', 'FALSE')
    is_pypy = sys.platform.startswith('pypy')
    
    return is_pypy and pure_python_env != 'PURE_PYTHON'