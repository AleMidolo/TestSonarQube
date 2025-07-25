import numpy as np

def make_array(shape, dtype=np.dtype("float32")):
    """
    返回一个具有指定形状和类型的全零数组。

    参数：
      shape : 元组  
        要创建的数组的形状  
      dtype : `numpy.dtype`  
        要创建的数组的数据类型  

    返回值：数组

    该函数创建一个具有指定形状和数据类型的数组。

      参数
      ----------
      shape : 元组
          要创建的数组的形状
      dtype : `numpy.dtype`
          要创建的数组的数据类型
    """
    return np.zeros(shape, dtype=dtype)