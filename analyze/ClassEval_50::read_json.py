def read_json(self, file_path):
    """
        读取一个 JSON 文件并返回数据。
        :param file_path: str，JSON 文件的路径。
        :return: dict，如果成功读取 JSON 文件则返回数据，如果在读取过程中发生错误则返回 -1。
                    如果文件不存在则返回 0。
        >>> json.read_json('test.json')
        {'name': 'test', 'age': 14}
        """
    if not os.path.exists(file_path):
        return 0
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except:
        return -1