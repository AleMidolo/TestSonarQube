def read_csv(self, file_name):
    """
    读取CSV文件并返回标题和数据
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) == 0:
                return ([], [])
            title = rows[0]
            data = rows[1:]
            return (title, data)
    except:
        return ([], [])