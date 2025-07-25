def _explore_zipfile(zip_path):
    """
    ज़िप पथ से पैकेजों का डेटा प्राप्त करता है।  

    फ़ाइलों को उनके XML बेसनाम (basename) के आधार पर समूहित करता है और डेटा को डिक्शनरी (dict) प्रारूप में लौटाता है।  

    पैरामीटर (Parameters)
    ----------
    zip_path : str  
        ज़िप फ़ाइल का पथ।  

    रिटर्न्स (Returns)
    -------
    dict
    """
    import zipfile
    import os
    from collections import defaultdict

    # Dictionary to store grouped files
    grouped_files = defaultdict(list)
    
    # Open zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Get list of all files in zip
        file_list = zip_ref.namelist()
        
        # Group files by their XML basename
        for file_name in file_list:
            # Get basename without extension
            base_name = os.path.splitext(os.path.basename(file_name))[0]
            
            # If file has XML basename (ends with .xml)
            if file_name.lower().endswith('.xml'):
                # Read file content
                with zip_ref.open(file_name) as f:
                    content = f.read()
                # Add to grouped files
                grouped_files[base_name].append({
                    'name': file_name,
                    'content': content
                })
            else:
                # For non-XML files, just store the name
                grouped_files[base_name].append({
                    'name': file_name,
                    'content': None
                })
    
    return dict(grouped_files)