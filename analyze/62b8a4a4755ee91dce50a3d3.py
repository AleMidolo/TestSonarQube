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

    # 检查是否存在歧义
    utc_offset_alt = self.utcoffset(local_dt - dst_offset)
    if utc_offset_alt is None:
        return local_dt

    if utc_offset != utc_offset_alt:
        # 存在歧义，检查是否在"折叠"状态
        if utc_offset > utc_offset_alt:
            # 从夏令时转换到标准时间
            fold = 1
        else:
            # 从标准时间转换到夏令时
            fold = 0
        return local_dt.replace(fold=fold)

    return local_dt