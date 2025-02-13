def _explore_folder(folder):
    import os
    from collections import defaultdict

    def _group_files_by_xml_filename(files):
        grouped_files = defaultdict(list)
        for file in files:
            if file.endswith('.xml'):
                basename = os.path.splitext(file)[0]
                grouped_files[basename].append(file)
        return dict(grouped_files)

    files = os.listdir(folder)
    return _group_files_by_xml_filename(files)