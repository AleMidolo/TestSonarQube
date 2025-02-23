def deep_merge_nodes(nodes):
    """
    合并任何与重复键对应的节点值并返回结果。如果存在具有非 `MappingNode` 值的冲突键，则保留最后一个值。

    给定一个嵌套的 borgmatic 配置数据结构，其形式为一个元组列表：
    (
          ruamel.yaml.nodes.ScalarNode as a key,
          ruamel.yaml.nodes.MappingNode or other Node as a value,
    ),

    对任何与重复键对应的节点值进行深度合并，并返回合并后的结果。如果存在具有非 `MappingNode` 值（例如整数或字符串）的冲突键，则以最后一个值为准。

    例如，给定以下节点值：
    [
          (
              ScalarNode(tag='tag:yaml.org,2002:str', value='retention'),
              MappingNode(tag='tag:yaml.org,2002:map', value=[
                  (
                      ScalarNode(tag='tag:yaml.org,2002:str', value='keep_hourly'),
                      ScalarNode(tag='tag:yaml.org,2002:int', value='24')
                  ),
                  (
                      ScalarNode(tag='tag:yaml.org,2002:str', value='keep_daily'),
                      ScalarNode(tag='tag:yaml.org,2002:int', value='7')
                  ),
              ]),
          ),
          (
              ScalarNode(tag='tag:yaml.org,2002:str', value='retention'),
              MappingNode(tag='tag:yaml.org,2002:map', value=[
                  (
                      ScalarNode(tag='tag:yaml.org,2002:str', value='keep_daily'),
                      ScalarNode(tag='tag:yaml.org,2002:int', value='5')
                  ),
              ]),
          ),
    ]

    返回的结果将为：

    [
          (
              ScalarNode(tag='tag:yaml.org,2002:str', value='retention'),
              MappingNode(tag='tag:yaml.org,2002:map', value=[
                  (
                      ScalarNode(tag='tag:yaml.org,2002:str', value='keep_hourly'),
                      ScalarNode(tag='tag:yaml.org,2002:int', value='24')
                  ),
                  (
                      ScalarNode(tag='tag:yaml.org,2002:str', value='keep_daily'),
                      ScalarNode(tag='tag:yaml.org,2002:int', value='5')
                  ),
              ]),
          ),
    ]

    进行这样的深度合并的目的是支持例如将一个 borgmatic 配置文件合并到另一个文件中以便重用。通过这种方式，配置部分（如 "retention" 等）不会完全替换合并文件中对应的部分，而是进行合并。
    """
    from ruamel.yaml.nodes import ScalarNode, MappingNode

    merged = {}

    for key, value in nodes:
        key_value = key.value
        if key_value not in merged:
            merged[key_value] = value
        else:
            if isinstance(value, MappingNode):
                merged[key_value] = deep_merge(merged[key_value], value)
            else:
                merged[key_value] = value

    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]

def deep_merge(dict1, dict2):
    """Helper function to merge two MappingNode instances."""
    for key, value in dict2.value:
        if key in dict1.value:
            existing_value = dict1.value[key]
            if isinstance(existing_value, MappingNode) and isinstance(value, MappingNode):
                deep_merge(existing_value, value)
            else:
                dict1.value[key] = value
        else:
            dict1.value[key] = value
    return dict1