def get_parser_option_specs(self, command_name):
    """
    获取指定命令的所有选项

    :param command_name: 命令名称（如 main、virsh、ospd 等）
    :return: 所有命令选项的列表
    """
    # 获取指定命令的解析器
    parser = self.parsers.get(command_name)
    if not parser:
        return []
        
    # 存储所有选项
    options = []
    
    # 遍历解析器中的所有选项
    for action in parser._actions:
        # 跳过帮助选项
        if action.dest == 'help':
            continue
            
        # 获取选项名称
        option_names = []
        for opt_str in action.option_strings:
            if opt_str.startswith('--'):
                option_names.append(opt_str[2:])
            elif opt_str.startswith('-'):
                option_names.append(opt_str[1:])
                
        if not option_names:
            continue
            
        # 构建选项规格
        option_spec = {
            'names': option_names,
            'required': action.required,
            'help': action.help or '',
            'default': action.default,
            'type': action.type.__name__ if action.type else 'str'
        }
        
        options.append(option_spec)
        
    return options