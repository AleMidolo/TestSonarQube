def format(
    self,
    sql: AnyStr,
    params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    将 SQL 使用 `self._converter.convert` 方法进行转换

    将 SQL 查询从 in-style 参数转换为 out-style 参数。

    *sql*（类型：`str` 或 `bytes`）是 SQL 查询语句。

    *params*（类型：`~collections.abc.Mapping` 或 `~collections.abc.Sequence`）包含一组 in-style 参数。它将每个参数（类型：`str` 或 `int`）映射到对应的值。如果 `SQLParams.in_style` 是命名参数样式，那么 *params* 必须是一个 `~collections.abc.Mapping` 类型。如果 `SQLParams.in_style` 是序号参数样式，那么 **params** 必须是一个 `~collections.abc.Sequence` 类型。

    返回一个包含以下内容的元组（`tuple`）：

      - 格式化后的 SQL 查询（类型：`str` 或 `bytes`）。

      - 转换后的 out-style 参数集合（类型：`dict` 或 `list`）。
    """
    # 检查参数类型是否匹配样式
    if self.in_style.is_named:
        if not isinstance(params, Mapping):
            raise TypeError("Named parameter style requires a mapping for params")
    else:
        if not isinstance(params, Sequence) or isinstance(params, (str, bytes)):
            raise TypeError("Positional parameter style requires a sequence for params")

    # 初始化输出参数集合
    out_params: Union[Dict[Union[str, int], Any], List[Any]]
    out_params = {} if self.out_style.is_named else []
    
    # 初始化参数计数器和SQL构建器
    param_count = 0
    formatted_sql = sql
    
    if self.in_style.is_named:
        # 处理命名参数
        for param_name, value in params.items():
            # 生成输出参数名
            out_name = self.out_style.format_param(param_count) if self.out_style.is_named else param_count
            
            # 转换参数值
            converted_value = self._converter.convert(value)
            
            # 替换SQL中的参数占位符
            formatted_sql = formatted_sql.replace(
                self.in_style.format_param(param_name),
                self.out_style.format_param(out_name)
            )
            
            # 存储转换后的参数
            if self.out_style.is_named:
                out_params[out_name] = converted_value
            else:
                out_params.append(converted_value)
                
            param_count += 1
    else:
        # 处理序号参数
        for i, value in enumerate(params):
            # 生成输出参数名
            out_name = self.out_style.format_param(i) if self.out_style.is_named else i
            
            # 转换参数值
            converted_value = self._converter.convert(value)
            
            # 替换SQL中的参数占位符
            formatted_sql = formatted_sql.replace(
                self.in_style.format_param(i),
                self.out_style.format_param(out_name)
            )
            
            # 存储转换后的参数
            if self.out_style.is_named:
                out_params[out_name] = converted_value
            else:
                out_params.append(converted_value)
    
    return formatted_sql, out_params