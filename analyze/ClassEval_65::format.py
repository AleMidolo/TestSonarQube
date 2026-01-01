def format(self, x):
    """
        Convierte un número en formato de palabras
        :param x: int o float, el número que se va a convertir en formato de palabras
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "CIENTO VEINTITRÉS MIL CUATROCIENTOS CINCUENTA Y SEIS SOLAMENTE"
        """
    if isinstance(x, int):
        x = str(x)
    elif isinstance(x, float):
        x = str(x)
    else:
        raise ValueError('Input must be an integer or float.')
    lstr, rstr = (x.split('.') + [''])[:2]
    lstrrev = lstr[::-1]
    a = [''] * 5
    if len(lstrrev) % 3 == 1:
        lstrrev += '00'
    elif len(lstrrev) % 3 == 2:
        lstrrev += '0'
    lm = ''
    for i in range(len(lstrrev) // 3):
        a[i] = lstrrev[3 * i:3 * i + 3][::-1]
        if a[i] != '000':
            lm = self.trans_three_spanish(a[i]) + ' ' + self.parse_more_spanish(i) + ' ' + lm
        else:
            lm += self.trans_three_spanish(a[i])
    xs = f'Y CENTAVOS {self.trans_two_spanish(rstr)} ' if rstr else ''
    if not lm.strip():
        return 'CERO SOLAMENTE'
    else:
        return f'{lm.strip()} {xs}SOLAMENTE'