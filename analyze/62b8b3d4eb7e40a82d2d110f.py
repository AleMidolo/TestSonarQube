import os
import sys

def _should_attempt_c_optimizations():
    """
    यदि हमें C अनुकूलन का प्रयास करना चाहिए, तो एक सत्य मान लौटाएं।  

    यह इस बात को ध्यान में रखता है कि क्या हम PyPy पर हैं और `_use_c_impl` में परिभाषित ``PURE_PYTHON`` पर्यावरण चर का मान क्या है।
    """
    # Check if we are running on PyPy
    is_pypy = hasattr(sys, 'pypy_version_info')
    
    # Check the value of the PURE_PYTHON environment variable
    pure_python = os.getenv('PURE_PYTHON', '').lower() in ('1', 'true', 'yes')
    
    # Return True if not on PyPy and PURE_PYTHON is not set to True
    return not is_pypy and not pure_python