def _fromutc(self, dt):
    """
    给定一个特定时区的日期时间，计算在新时区的日期时间。

    给定一个带有时区信息的日期时间对象，计算在新时区的带有时区信息的日期时间。

    由于这是我们*明确知道*日期时间对象没有歧义的唯一时刻，我们利用这个机会来判断该日期时间是否存在歧义，并且是否处于“折叠”状态（例如，如果这是歧义日期时间的第一个按时间顺序出现的实例）。

    :param dt: 一个带有时区信息的 :class:`datetime.datetime` 对象。
    """
    if dt.tzinfo is not self:
        raise ValueError("dt.tzinfo is not self")
    
    # Convert the datetime to the new timezone
    new_dt = dt.astimezone(self)
    
    # Check if the new datetime is ambiguous
    if self.is_ambiguous(new_dt):
        # If ambiguous, check if it's the first occurrence
        if self._fold and self._fold == 1:
            # If it's the first occurrence, return the datetime as is
            return new_dt
        else:
            # Otherwise, adjust the datetime to the second occurrence
            return new_dt.replace(fold=1)
    else:
        # If not ambiguous, return the datetime as is
        return new_dt