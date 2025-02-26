import subprocess

def addignored(ignored):
    """
    1. गिट कमांड का उपयोग करें ताकि सभी फ़ाइल नाम प्राप्त किए जा सकें।
    2. प्राप्त फ़ाइल नामों को एक सूची (list) में बदलें।
    3. सूची को केवल उन फ़ाइलों के लिए छांटें जो `.gitignore` में अनदेखी (ignored) की गई हैं।
    4. उन फ़ाइल नामों को एक स्ट्रिंग में बदलें, जिसमें प्रत्येक नाम अल्पविराम (comma) से अलग हो।  
    5. अंतिम परिणाम को फ़ंक्शन से लौटाएं।
    """
    # Get all file names from git
    result = subprocess.run(['git', 'ls-files'], stdout=subprocess.PIPE, text=True)
    all_files = result.stdout.splitlines()

    # Read the .gitignore file
    with open('.gitignore', 'r') as f:
        ignored_patterns = f.read().splitlines()

    # Filter the files that are ignored
    ignored_files = [file for file in all_files if any(pattern in file for pattern in ignored_patterns)]

    # Join the ignored files into a comma-separated string
    return ','.join(ignored_files)