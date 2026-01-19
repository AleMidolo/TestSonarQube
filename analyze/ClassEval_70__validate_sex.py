def _validate_sex(self, sex: str) -> str:
    """
        Valida el sexo y lo devuelve. Si el sexo no es Hombre, Mujer o UGM, se establece en None.
        :param sex: str, el sexo a validar
        :return: str, el sexo validado o None si es inválido
        """
    valid_sexes = ['Hombre', 'Mujer', 'UGM']
    if sex in valid_sexes:
        return sex
    return None