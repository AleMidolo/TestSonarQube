def _fromutc(self, dt):
    """
    给定一个特定时区的日期时间，计算在新时区的日期时间。

    给定一个带有时区信息的日期时间对象，计算在新时区的带有时区信息的日期时间。

    由于这是我们*明确知道*日期时间对象没有歧义的唯一时刻，我们利用这个机会来判断该日期时间是否存在歧义，并且是否处于“折叠”状态（例如，如果这是歧义日期时间的第一个按时间顺序出现的实例）。

    :param dt: 一个带有时区信息的 :class:`datetime.datetime` 对象。
    """
    if dt.tzinfo is None:
        raise ValueError("The input datetime must be timezone-aware.")

    # Convert the datetime to the new timezone
    new_dt = dt.astimezone(self)

    # Check if the datetime is ambiguous
    if self.is_ambiguous(new_dt):
        # If ambiguous, set the fold attribute to 0 (first occurrence)
        new_dt = new_dt.replace(fold=0)

    return new_dt