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
            
            # If file has XML basename (ends with .xml when extension added back)
            if file_name.endswith('.xml'):
                # Use base_name as key and store full file path
                grouped_files[base_name].append(file_name)
                
                # Add any related files with same basename
                for related_file in file_list:
                    if related_file != file_name and \
                       os.path.splitext(os.path.basename(related_file))[0] == base_name:
                        grouped_files[base_name].append(related_file)
    
    return dict(grouped_files)