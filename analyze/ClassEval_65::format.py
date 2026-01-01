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
    words = self.format_string(x)
    spanish_words = words.replace('ONE', 'UNO').replace('TWO', 'DOS').replace('THREE', 'TRES').replace('FOUR', 'CUATRO').replace('FIVE', 'CINCO').replace('SIX', 'SEIS').replace('SEVEN', 'SIETE').replace('EIGHT', 'OCHO').replace('NINE', 'NUEVE').replace('TEN', 'DIEZ').replace('ELEVEN', 'ONCE').replace('TWELVE', 'DOCE').replace('THIRTEEN', 'TRECE').replace('FOURTEEN', 'CATORCE').replace('FIFTEEN', 'QUINCE').replace('SIXTEEN', 'DIECISEIS').replace('SEVENTEEN', 'DIECISIETE').replace('EIGHTEEN', 'DIECIOCHO').replace('NINETEEN', 'DIECINUEVE').replace('TWENTY', 'VEINTE').replace('THIRTY', 'TREINTA').replace('FORTY', 'CUARENTA').replace('FIFTY', 'CINCUENTA').replace('SIXTY', 'SESENTA').replace('SEVENTY', 'SETENTA').replace('EIGHTY', 'OCHENTA').replace('NINETY', 'NOVENTA').replace('HUNDRED', 'CIENTO').replace('THOUSAND', 'MIL').replace('MILLION', 'MILLÓN').replace('BILLION', 'MIL MILLONES').replace('ONLY', 'SOLAMENTE').replace('AND', 'Y').strip()
    return spanish_words