def book_room(self, room_type, room_number, name):
    """
    检查是否有任何指定类型的房间可用。
    如果房间数量足够，修改 available_rooms 和 booked_rooms 并完成预订，否则预订失败。
    :param room_type: str
    :param room_number: int，预期预订的指定类型房间的数量
    :param name: str，客人姓名
    :return: 如果即将预订的房间数量不超过剩余房间，返回 str 'Success!'
            如果超过但可用房间数量不为零，返回 int（该房间类型的剩余数量）。
            如果超过且数量为零或 room_type 不在 available_room 中，返回 False。
    >>> hotel = Hotel('和平酒店', {'single': 5, 'double': 3})
    >>> hotel.book_room('single', 1, '客人 1')
    'Success!'
    >>> hotel.book_room('single', 5, '客人 1')
    4
    >>> hotel.book_room('single', 4, '客人 1')
    'Success!'
    >>> hotel.book_room('single', 1, '客人 1')
    False
    >>> hotel.book_room('triple', 1, '客人 1')
    False
    """
    # 检查房间类型是否存在
    if room_type not in self.available_rooms:
        return False
    
    # 获取当前可用房间数量
    available_count = self.available_rooms[room_type]
    
    # 如果可用房间数量为零
    if available_count == 0:
        return False
    
    # 如果请求的房间数量不超过可用房间数量
    if room_number <= available_count:
        # 更新可用房间数量
        self.available_rooms[room_type] -= room_number
        
        # 更新已预订房间记录
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = []
        self.booked_rooms[room_type].append({name: room_number})
        
        return 'Success!'
    else:
        # 请求的房间数量超过可用数量，但可用数量不为零
        return available_count