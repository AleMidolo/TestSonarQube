def write_json(self, data, file_path):
    """
        将数据写入 JSON 文件并保存到给定路径。

        :param data: dict，要写入 JSON 文件的数据。
        :param file_path: str，JSON 文件的路径。
        :return: 如果写入过程成功则返回 1，若在写入过程中发生错误则返回 -1。
        >>> json.write_json({'key1': 'value1', 'key2': 'value2'}, 'test.json')
        1
        >>> json.read_json('test.json')
        {'key1': 'value1', 'key2': 'value2'}
        """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
        return 1
    except:
        return -1