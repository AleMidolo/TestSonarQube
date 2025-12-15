def add_seconds(self, seconds):
    """
    Add the specified number of seconds to the current time
    :param seconds: int, number of seconds to add
    :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
    >>> timeutils = TimeUtils()
    >>> timeutils.add_seconds(600)
    "19:29:22"
    """
    
    new_time = self.datetime + datetime.timedelta(seconds=seconds)
    return new_time.strftime("%H:%M:%S")