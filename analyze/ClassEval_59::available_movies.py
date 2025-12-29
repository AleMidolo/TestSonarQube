def available_movies(self, start_time, end_time):
    """
        निर्दिष्ट समय सीमा के भीतर उपलब्ध फिल्मों की सूची प्राप्त करें
        :param start_time: str, HH:MM प्रारूप में प्रारंभ समय
        :param end_time: str, HH:MM प्रारूप में समाप्ति समय
        :return: list of str, उपलब्ध फिल्मों के नाम
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.available_movies('12:00', '22:00')
        ['Batman']
        """
    start_dt = datetime.strptime(start_time, '%H:%M')
    end_dt = datetime.strptime(end_time, '%H:%M')
    available = []
    for movie in self.movies:
        if movie['start_time'] <= end_dt and movie['end_time'] >= start_dt:
            available.append(movie['name'])
    return available