import subprocess

def addignored(ignored):
    # Step 1: Use git command to get all file names
    result = subprocess.run(['git', 'ls-files'], stdout=subprocess.PIPE)
    all_files = result.stdout.decode('utf-8').splitlines()
    
    # Step 2: Convert the file names into a list
    file_list = list(all_files)
    
    # Step 3: Filter the list to only include files that are ignored in .gitignore
    ignored_files = [file for file in file_list if file in ignored]
    
    # Step 4: Convert the file names into a string, separated by commas
    ignored_files_str = ','.join(ignored_files)
    
    # Step 5: Return the final result
    return ignored_files_str