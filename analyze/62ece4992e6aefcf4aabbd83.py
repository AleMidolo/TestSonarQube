import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को कॉल करें।
    
    :param commands: कमांड(s) की सूची
    :param args: कमांड के लिए आर्ग्युमेंट्स
    :param cwd: कमांड को रन करने के लिए वर्किंग डायरेक्टरी
    :param verbose: यदि True, तो कमांड का आउटपुट प्रिंट करें
    :param hide_stderr: यदि True, तो स्टडरर को छुपाएं
    :param env: एनवायरनमेंट वेरिएबल्स
    :return: सबप्रोसेस का रिजल्ट
    """
    full_command = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    if verbose:
        print(f"Running command: {' '.join(full_command)}")
    
    result = subprocess.run(
        full_command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=stderr,
        text=True
    )
    
    if verbose and result.stdout:
        print(result.stdout)
    
    return result