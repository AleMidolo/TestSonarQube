def _validate_sex(self, sex: str) -> str:
    """
        Valida il sesso e lo restituisce. Se il sesso non è Uomo, Donna o UGM, imposta a None.
        :param sex: str, il sesso da validare
        :return: str, il sesso validato o None se non valido
        """
    valid_sexes = {'Uomo', 'Donna', 'UGM'}
    if sex in valid_sexes:
        return sex
    return None