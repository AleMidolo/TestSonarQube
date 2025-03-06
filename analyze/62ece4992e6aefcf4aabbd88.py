import numpy as np

def make_array(shape, dtype=np.dtype("float32")):
    """
    Funzione per creare un array con una forma e un tipo di dato specificati.

    Parametri
    ----------
    shape : tuple
        forma dell'array da creare
    dtype : `numpy.dtype`
        tipo di dato dell'array da creare

    Restituisce
    -------
    numpy.ndarray
        array con la forma e il tipo di dato specificati
    """
    return np.zeros(shape, dtype=dtype)