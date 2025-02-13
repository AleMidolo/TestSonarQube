def _explore_zipfile(zip_path):
    import zipfile
    from collections import defaultdict
    import os

    def _group_files_by_xml_filename(files):
        grouped_files = defaultdict(list)
        for file in files:
            if file.endswith('.xml'):
                basename = os.path.basename(file).split('.')[0]
                grouped_files[basename].append(file)
        return dict(grouped_files)

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        file_list = zip_file.namelist()
        grouped_data = _group_files_by_xml_filename(file_list)

    return grouped_data