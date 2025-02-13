def _eval_file(prefix, file_path):
    import os

    if not file_path.startswith(prefix):
        return None

    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == '.xml':
        return None

    component_id = os.path.basename(file_path).split('.')[0]
    
    if file_extension == '.pdf':
        return {'component_id': component_id, 'file_path': file_path}
    else:
        ftype = file_extension[1:]  # Remove the dot from the extension
        return {'component_id': component_id, 'file_path': file_path, 'ftype': ftype}