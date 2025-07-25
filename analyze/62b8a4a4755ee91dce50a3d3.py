def fromutc(self, dt):
    """
    给定一个在给定时区中带有时区信息的日期时间对象，计算在新时区的带有时区信息的日期时间。

    由于这是我们*明确知道*日期时间对象没有歧义的唯一时刻，我们利用这个机会来判断该日期时间是否存在歧义，并且是否处于"折叠"状态（例如，如果这是歧义日期时间的第一个按时间顺序出现的实例）。

    :param dt: 一个带有时区信息的 :class:`datetime.datetime` 对象。
    """
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)

    utc = dt.replace(tzinfo=None)

    # 计算本地时间的偏移量
    local_offset = self._transition_info[self._find_trans_idx(utc)][0]
    
    # 转换为本地时间
    local_dt = utc + local_offset

    # 检查是否在DST转换期间
    idx = self._find_trans_idx(local_dt)
    trans_info = self._transition_info[idx]
    
    # 检查是否存在歧义
    if idx > 0:
        prev_info = self._transition_info[idx - 1]
        if prev_info[0] > trans_info[0]:  # 从DST转换到标准时间
            fold_delta = prev_info[0] - trans_info[0]
            if local_dt - fold_delta <= local_dt < local_dt + fold_delta:
                # 在折叠期间
                return local_dt.replace(fold=1, tzinfo=self)
    
    return local_dt.replace(tzinfo=self)