def _fromutc(self, dt):
    """
    给定一个特定时区的日期时间，计算在新时区的日期时间。

    给定一个带有时区信息的日期时间对象，计算在新时区的带有时区信息的日期时间。

    由于这是我们*明确知道*日期时间对象没有歧义的唯一时刻，我们利用这个机会来判断该日期时间是否存在歧义，并且是否处于“折叠”状态（例如，如果这是歧义日期时间的第一个按时间顺序出现的实例）。

    :param dt: 一个带有时区信息的 :class:`datetime.datetime` 对象。
    """
    # 检查输入的日期时间对象是否为带有时区信息的datetime对象
    if dt.tzinfo is None:
        raise ValueError("dt must be a timezone-aware datetime object")

    # 获取当前时区的UTC偏移量
    utc_offset = self.utcoffset(dt)

    # 计算新的UTC时间
    utc_dt = dt - utc_offset

    # 将UTC时间转换为新的时区时间
    new_dt = utc_dt.astimezone(self)

    # 检查是否存在歧义
    if new_dt.dst() != timedelta(0):
        # 如果有夏令时，检查是否处于折叠状态
        if new_dt < dt:
            # 这是第一个按时间顺序出现的实例
            return new_dt
        else:
            raise ValueError("Ambiguous datetime detected")

    return new_dt