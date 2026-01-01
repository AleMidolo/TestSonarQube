@staticmethod
def check(args):
    """
        Verifica si los parámetros son legales, args debe ser mayor o igual a 0 y debe ser par; de lo contrario, se genera un ValueError.
        :param args: Parámetros a verificar, lista.
        :return: Ninguno.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: 3 no es par
        """
    for arg in args:
        if arg < 0:
            raise ValueError(f'{arg} es menor que 0')
        if arg % 2 != 0:
            raise ValueError(f'{arg} no es par')