def select_filenames_by_prefix(prefix, files):
    """
    दस्तावेज़ पैकेज से संबंधित फ़ाइलें प्राप्त करें।

    `files` सूची में से उन फ़ाइलों को लौटाएं जिनके नाम `prefix` से शुरू होते हैं।

    पैरामीटर्स (Parameters)
    ----------
    `prefix` : str  
        फ़ाइल नाम का प्रीफ़िक्स (Prefix)  

    `files` : str list  
        फ़ाइल पथों (File paths) की सूची  

    रिटर्न्स (Returns)
    -------
    list  
        उन फ़ाइल पथों की सूची, जिनके बेसनाम (basename) फ़ाइलें दिए गए प्रीफ़िक्स से मेल खाती हैं।  
    """
    return [file for file in files if file.split('/')[-1].startswith(prefix)]