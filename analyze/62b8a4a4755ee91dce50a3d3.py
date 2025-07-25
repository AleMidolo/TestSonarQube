def fromutc(self, dt):
    """
    给定一个在给定时区中带有时区信息的日期时间对象，计算在新时区的带有时区信息的日期时间。

    由于这是我们*明确知道*日期时间对象没有歧义的唯一时刻，我们利用这个机会来判断该日期时间是否存在歧义，并且是否处于"折叠"状态（例如，如果这是歧义日期时间的第一个按时间顺序出现的实例）。

    :param dt: 一个带有时区信息的 :class:`datetime.datetime` 对象。
    """
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)

    utc_offset = self._transition_info[self._find_trans_idx(dt.replace(tzinfo=None))][0]
    
    # 计算本地时间
    local_dt = dt + utc_offset
    
    # 检查是否在DST转换期间
    idx = self._find_trans_idx(local_dt.replace(tzinfo=None))
    trans_info = self._transition_info[idx]
    
    # 检查是否存在歧义
    if idx > 0:
        prev_info = self._transition_info[idx - 1]
        if prev_info[0] > trans_info[0]:  # 如果是从DST转向标准时间
            ambiguous_start = local_dt - (prev_info[0] - trans_info[0])
            if ambiguous_start <= local_dt < (ambiguous_start + (prev_info[0] - trans_info[0])):
                # 在歧义期间，使用第一次出现的时间
                return local_dt.replace(tzinfo=self)
    
    # 检查是否在"空洞"期间
    if idx > 0:
        prev_info = self._transition_info[idx - 1]
        if prev_info[0] < trans_info[0]:  # 如果是从标准时间转向DST
            gap_start = local_dt - (trans_info[0] - prev_info[0])
            if gap_start <= local_dt < (gap_start + (trans_info[0] - prev_info[0])):
                # 在"空洞"期间，调整到转换后的时间
                return (local_dt + (trans_info[0] - prev_info[0])).replace(tzinfo=self)
    
    return local_dt.replace(tzinfo=self)