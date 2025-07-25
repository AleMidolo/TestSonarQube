import os

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    给定一个渲染后的配置 YAML，将其写入目标文件。
      如果文件已存在且 `overwrite` 参数为假，则在写入任何内容之前中止操作。
      如果文件不存在，则创建它。
      否则，将内容写入文件。

    返回值：`None`

    给定一个目标配置文件名和渲染的配置 YAML，将其写入文件。必要时创建包含的目录。但如果文件已存在且 `overwrite` 参数为假，则在写入任何内容之前中止操作。
    """
    # Create the directory if it does not exist
    directory = os.path.dirname(config_filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Check if the file exists and overwrite is False
    if os.path.exists(config_filename) and not overwrite:
        return None

    # Write the rendered configuration to the file
    with open(config_filename, 'w') as config_file:
        config_file.write(rendered_config)

    # Set the file permissions
    os.chmod(config_filename, mode)