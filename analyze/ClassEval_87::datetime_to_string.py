def datetime_to_string(self, datetime):
    """
        Converti un'istanza di datetime in una stringa
        :param datetime: l'istanza di datetime da convertire
        :return: stringa, stringa di tempo convertita
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
    format = '%Y-%m-%d %H:%M:%S'
    return datetime.strftime(format)