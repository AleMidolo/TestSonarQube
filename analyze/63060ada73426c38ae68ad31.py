def _convert_non_cli_args(self, parser_name, values_dict):
    """
    通过修改 values_dict 参数将参数转换为正确的类型。

    默认情况下，所有的值都是字符串。

    :param parser_name: 命令名称，例如 main、virsh、ospd 等
    :param values_dict: 包含参数的字典
    """
    if parser_name == 'main':
        if 'port' in values_dict:
            values_dict['port'] = int(values_dict['port'])
        if 'timeout' in values_dict:
            values_dict['timeout'] = float(values_dict['timeout'])
        if 'verbose' in values_dict:
            values_dict['verbose'] = values_dict['verbose'].lower() == 'true'
    
    elif parser_name == 'virsh':
        if 'memory' in values_dict:
            values_dict['memory'] = int(values_dict['memory'])
        if 'cpu' in values_dict:
            values_dict['cpu'] = int(values_dict['cpu'])
        if 'autostart' in values_dict:
            values_dict['autostart'] = values_dict['autostart'].lower() == 'true'
    
    elif parser_name == 'ospd':
        if 'interval' in values_dict:
            values_dict['interval'] = float(values_dict['interval'])
        if 'retries' in values_dict:
            values_dict['retries'] = int(values_dict['retries'])
        if 'debug' in values_dict:
            values_dict['debug'] = values_dict['debug'].lower() == 'true'
    
    # 可以根据需要添加更多的 parser_name 和对应的转换逻辑