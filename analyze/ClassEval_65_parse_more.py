def parse_more(self, i):
    """
    根据索引解析千/百万/十亿后缀
    :param i: int，表示数量级的索引（千、百万、十亿）
    :return: str，数量级对应的后缀
    >>> formatter = NumberWordFormatter()
    >>> formatter.parse_more(1)
    "THOUSAND"
    """
    magnitude_map = {
        1: "THOUSAND",
        2: "MILLION",
        3: "BILLION"
    }
    return magnitude_map.get(i, "")