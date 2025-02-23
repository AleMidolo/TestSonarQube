import subprocess

def addignored(ignored):
    """
    1. गिट कमांड का उपयोग करें ताकि सभी फ़ाइल नाम प्राप्त किए जा सकें।
    2. प्राप्त फ़ाइल नामों को एक सूची (list) में बदलें।
    3. सूची को केवल उन फ़ाइलों के लिए छांटें जो `.gitignore` में अनदेखी (ignored) की गई हैं।
    4. उन फ़ाइल नामों को एक स्ट्रिंग में बदलें, जिसमें प्रत्येक नाम अल्पविराम (comma) से अलग हो।  
    5. अंतिम परिणाम को फ़ंक्शन से लौटाएं।
    """
    # Step 1: Get all file names using git command
    result = subprocess.run(['git', 'ls-files'], stdout=subprocess.PIPE, text=True)
    all_files = result.stdout.splitlines()

    # Step 2: Convert to list (already in list form)

    # Step 3: Filter the list for ignored files
    ignored_files = []
    with open('.gitignore', 'r') as f:
        ignored_patterns = f.read().splitlines()
    
    for file in all_files:
        for pattern in ignored_patterns:
            if pattern in file:
                ignored_files.append(file)
                break

    # Step 4: Convert the list of ignored files to a comma-separated string
    ignored_files_string = ','.join(ignored_files)

    # Step 5: Return the final result
    return ignored_files_string