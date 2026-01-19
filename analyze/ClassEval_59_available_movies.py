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
    def time_to_minutes(time_str):
        """将 HH:MM 格式的时间转换为分钟数"""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)
    
    available = []
    
    # 假设 self.movies 是一个字典，存储电影信息
    # 键为电影名称，值为包含电影信息的字典（包括 start_time 和 end_time）
    for movie_name, movie_info in self.movies.items():
        movie_start = time_to_minutes(movie_info['start_time'])
        movie_end = time_to_minutes(movie_info['end_time'])
        
        # 检查电影的放映时间是否在指定的时间范围内
        if movie_start >= start_minutes and movie_end <= end_minutes:
            available.append(movie_name)
    
    return available