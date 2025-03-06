import os
import mimetypes

def _eval_file(prefix, file_path):
    """
    识别给定文件的类型。如果文件与给定的前缀不匹配，或者文件类型是 XML，则返回 `None`。  
    如果文件类型是 "pdf"，返回一个包含键 `component_id` 和 `file_path` 的字典。  
    如果文件类型不是 "pdf"，返回一个包含键 `component_id`、`file_path`、`ftype` 和 `file_path` 的字典。

    识别包中的文件类型：`asset` 或 `rendition`。

    识别包中的文件类型，并使用文件的类型和路径更新 `packages`。

    参数
    ----------
    prefix: `str`  
      XML 文件的名称（不带扩展名）。

    filename: `str`  
      文件名。

    file_folder: `str`  
      文件所在的文件夹。

    返回值
    ----------
    dict  
    """
    # 获取文件名和扩展名
    file_name = os.path.basename(file_path)
    file_ext = os.path.splitext(file_name)[1].lower()

    # 如果文件扩展名是 .xml，返回 None
    if file_ext == '.xml':
        return None

    # 获取文件类型
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        return None

    # 如果文件类型是 PDF
    if mime_type == 'application/pdf':
        return {
            'component_id': prefix,
            'file_path': file_path
        }
    else:
        # 识别文件类型是 asset 还是 rendition
        if 'asset' in file_name.lower():
            ftype = 'asset'
        elif 'rendition' in file_name.lower():
            ftype = 'rendition'
        else:
            ftype = 'unknown'

        return {
            'component_id': prefix,
            'file_path': file_path,
            'ftype': ftype,
            'mime_type': mime_type
        }