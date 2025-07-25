import numpy as np

def make_array(shape, dtype=np.dtype("float32")):
    """
    यह फ़ंक्शन एक ऐरे बनाता है जिसमें दिए गए आकार (shape) और डेटा प्रकार (dtype) का उपयोग किया जाता है।

    पैरामीटर (Parameters):
    - shape : ट्यूपल  
      बनाने वाले ऐरे का आकार (shape)।

    - dtype : `numpy.dtype`  
      बनाने वाले ऐरे का डेटा प्रकार (data-type)।
    """
    return np.zeros(shape, dtype=dtype)