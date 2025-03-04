def _fromutc(self, dt):
    """
    给定一个特定时区的日期时间，计算在新时区的日期时间。

    给定一个带有时区信息的日期时间对象，计算在新时区的带有时区信息的日期时间。

    由于这是我们*明确知道*日期时间对象没有歧义的唯一时刻，我们利用这个机会来判断该日期时间是否存在歧义，并且是否处于"折叠"状态（例如，如果这是歧义日期时间的第一个按时间顺序出现的实例）。

    :param dt: 一个带有时区信息的 :class:`datetime.datetime` 对象。
    """
    # 检查输入参数是否有效
    if dt.tzinfo is not self:
        raise ValueError("fromutc() requires a datetime with tzinfo is self")

    # 获取UTC偏移量
    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt

    # 计算本地时间
    local_dt = dt + utc_offset

    # 获取dst偏移量
    dst_offset = self.dst(local_dt)
    if dst_offset is None:
        return local_dt

    # 检查是否在DST转换期间
    fold = 0
    if dst_offset != self.dst(local_dt - dst_offset):
        # 我们在DST转换期间
        # 检查是否在重复时间段内
        utc_transition = dt + utc_offset - dst_offset
        local_transition = utc_transition + self.dst(utc_transition)
        
        if local_dt > local_transition:
            fold = 1

    # 返回最终结果，包含fold信息
    return local_dt.replace(fold=fold)