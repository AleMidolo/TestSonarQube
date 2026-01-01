def available_movies(self, start_time, end_time):
    """
        获取指定时间范围内可用电影的列表
        :param start_time: str, 开始时间，格式为 HH:MM
        :param end_time: str, 结束时间，格式为 HH:MM
        :return: list of str, 可用电影的名称
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.available_movies('12:00', '22:00')
        ['Batman']
        """
    start_time = datetime.strptime(start_time, '%H:%M')
    end_time = datetime.strptime(end_time, '%H:%M')
    available = []
    for movie in self.movies:
        if movie['start_time'] >= start_time and movie['end_time'] <= end_time:
            available.append(movie['name'])
    return available