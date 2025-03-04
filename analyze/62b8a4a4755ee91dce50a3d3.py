def fromutc(self, dt):
    """
    给定一个在给定时区中带有时区信息的日期时间对象，计算在新时区的带有时区信息的日期时间。

    由于这是我们*明确知道*日期时间对象没有歧义的唯一时刻，我们利用这个机会来判断该日期时间是否存在歧义，并且是否处于"折叠"状态（例如，如果这是歧义日期时间的第一个按时间顺序出现的实例）。

    :param dt: 一个带有时区信息的 :class:`datetime.datetime` 对象。
    """
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)

    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt

    # 计算本地时间
    local_dt = dt + utc_offset

    # 检查是否在DST转换期间
    dst_offset = self.dst(local_dt)
    if dst_offset is None:
        return local_dt

    # 检查是否存在歧义时间
    utc_offset_alt = self.utcoffset(local_dt - dst_offset)
    if utc_offset_alt is None:
        return local_dt

    if utc_offset != utc_offset_alt:
        # 存在歧义时间
        # 如果是向前跳转(spring forward)，返回第一个有效时间
        if utc_offset < utc_offset_alt:
            return local_dt + dst_offset
        # 如果是向后跳转(fall back)，返回第一个出现的时间
        else:
            return local_dt

    return local_dt