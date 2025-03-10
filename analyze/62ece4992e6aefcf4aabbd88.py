import numpy as np

def make_array(shape, dtype=np.dtype("float32")):
    """
    Devuelve un arreglo lleno de ceros con la forma y el tipo de datos especificados.

    Argumentos:
        shape : tuple
            Forma del arreglo a crear.
        dtype : `numpy.dtype`
            Tipo de datos del arreglo a crear.
    Retorno: array
    """
    return np.zeros(shape, dtype=dtype)