def _explore_folder(folder):
    """
    फ़ोल्डर से पैकेज का डेटा प्राप्त करें।  

    फ़ाइलों को उनके XML बेसनाम के आधार पर समूहित करता है और डेटा को डिक्शनरी (dict) प्रारूप में लौटाता है।  

    पैरामीटर  
    folder : str
        पैकेज का फ़ोल्डर।  

    रिटर्न्स  
    dict
    """
    import os
    from collections import defaultdict
    
    # Initialize dictionary to store grouped files
    grouped_files = defaultdict(list)
    
    # Walk through the folder
    for root, dirs, files in os.walk(folder):
        for file in files:
            # Get full file path
            file_path = os.path.join(root, file)
            
            # Get base name without extension
            base_name = os.path.splitext(file)[0]
            
            # Group files by their base names
            if file.lower().endswith(('.xml', '.pdf', '.txt')):
                grouped_files[base_name].append(file_path)
    
    # Convert defaultdict to regular dict
    return dict(grouped_files)