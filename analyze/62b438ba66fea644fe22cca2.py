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
        if isinstance(value, MappingNode):
            if key in merged:
                # Merge the existing mapping with the new one
                existing_mapping = merged[key]
                for sub_key, sub_value in value.value:
                    existing_mapping[sub_key] = sub_value
            else:
                merged[key] = value.value
        else:
            merged[key] = value

    return [(key, MappingNode(tag='tag:yaml.org,2002:map', value=list(merged[key].items()))) for key in merged]