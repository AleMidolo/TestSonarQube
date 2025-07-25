def fromutc(self, dt):
    """
    给定一个在给定时区中带有时区信息的日期时间对象，计算在新时区的带有时区信息的日期时间。

    由于这是我们*明确知道*日期时间对象没有歧义的唯一时刻，我们利用这个机会来判断该日期时间是否存在歧义，并且是否处于"折叠"状态（例如，如果这是歧义日期时间的第一个按时间顺序出现的实例）。

    :param dt: 一个带有时区信息的 :class:`datetime.datetime` 对象。
    """
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)

    utc = dt.replace(tzinfo=None)

    # 计算本地时间
    local = utc + self.utcoffset(utc)

    # 检查是否在DST转换期间
    if self.dst(local) != self.dst(utc):
        # 在DST转换期间,重新计算本地时间
        local = utc + self.utcoffset(local)
        
        # 再次检查DST状态
        if self.dst(local) != self.dst(utc):
            # 如果仍然不匹配,使用第一次计算的结果
            local = utc + self.utcoffset(utc)

    # 设置正确的时区信息
    return local.replace(tzinfo=self)