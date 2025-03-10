def fromutc(self, dt):
    """
    给定一个在给定时区中带有时区信息的日期时间对象，计算在新时区的带有时区信息的日期时间。

    由于这是我们*明确知道*日期时间对象没有歧义的唯一时刻，我们利用这个机会来判断该日期时间是否存在歧义，并且是否处于“折叠”状态（例如，如果这是歧义日期时间的第一个按时间顺序出现的实例）。

    :param dt: 一个带有时区信息的 :class:`datetime.datetime` 对象。
    """
    if dt.tzinfo is not self:
        raise ValueError("fromutc: dt.tzinfo is not self")
    
    # Convert dt to UTC
    dt = dt.replace(tzinfo=None)
    dt = dt - self.utcoffset(dt)
    
    # Convert to local time
    dt = dt + self.utcoffset(dt)
    
    # Check for ambiguity
    if self.is_ambiguous(dt):
        # If ambiguous, return the first occurrence
        dt = self._fold_first(dt)
    
    return dt.replace(tzinfo=self)