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

    file_path: `str`  
      文件的完整路径。

    返回值
    ----------
    dict  
    """
    # 获取文件名和扩展名
    file_name = os.path.basename(file_path)
    file_prefix, file_ext = os.path.splitext(file_name)
    
    # 如果文件前缀与给定的前缀不匹配，或者文件类型是 XML，则返回 None
    if file_prefix != prefix or file_ext.lower() == '.xml':
        return None
    
    # 获取文件的 MIME 类型
    mime_type, _ = mimetypes.guess_type(file_path)
    
    # 如果文件类型是 PDF
    if mime_type == 'application/pdf':
        return {
            'component_id': prefix,
            'file_path': file_path
        }
    else:
        # 识别文件类型是 asset 还是 rendition
        ftype = 'asset' if 'asset' in file_path.lower() else 'rendition'
        
        return {
            'component_id': prefix,
            'file_path': file_path,
            'ftype': ftype,
            'mime_type': mime_type
        }