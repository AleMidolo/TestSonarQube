def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    给定一个渲染后的配置 YAML，将其写入目标文件。
      如果文件已存在且 `overwrite` 参数为假，则在写入任何内容之前中止操作。
      如果文件不存在，则创建它。
      否则，将内容写入文件。

    返回值：`None`

    给定一个目标配置文件名和渲染的配置 YAML，将其写入文件。必要时创建包含的目录。但如果文件已存在且 `overwrite` 参数为假，则在写入任何内容之前中止操作。
    """
    import os
    import pathlib

    # 创建目标文件所在的目录
    target_dir = os.path.dirname(config_filename)
    if target_dir:
        pathlib.Path(target_dir).mkdir(parents=True, exist_ok=True)

    # 检查文件是否已存在
    if os.path.exists(config_filename) and not overwrite:
        return None

    # 写入配置文件
    with open(config_filename, 'w') as f:
        f.write(rendered_config)

    # 设置文件权限
    os.chmod(config_filename, mode)

    return None