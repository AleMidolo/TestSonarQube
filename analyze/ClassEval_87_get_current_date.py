def get_current_date(self):
    """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        >>> timeutils.get_current_date()
        "2023-06-14"
        """
    return self.datetime.strftime('%Y-%m-%d')