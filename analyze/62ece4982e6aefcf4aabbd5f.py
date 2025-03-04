def paging(response, max_results):
    """
    根据 max_results 指定的长度返回每个响应。

    以分页方式返回 WAPI 响应。

    参数：
        response (list): WAPI 响应数据。
        max_results (int): 每页返回的最大对象数量。
    返回值：
        一个生成器对象，按页分割 WAPI 响应数据。
    """
    for i in range(0, len(response), max_results):
        yield response[i:i + max_results]