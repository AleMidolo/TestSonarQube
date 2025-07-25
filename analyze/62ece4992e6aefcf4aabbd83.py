import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को कॉल करें।
    
    :param commands: कमांड(s) की सूची
    :param args: कमांड के लिए आर्ग्युमेंट्स
    :param cwd: कमांड को रन करने के लिए वर्किंग डायरेक्टरी
    :param verbose: यदि True है, तो कमांड का आउटपुट प्रिंट करें
    :param hide_stderr: यदि True है, तो stderr को छुपाएं
    :param env: पर्यावरण वेरिएबल्स
    :return: कमांड का रिटर्न कोड
    """
    full_command = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    process = subprocess.Popen(
        full_command,
        cwd=cwd,
        stdout=subprocess.PIPE if verbose else None,
        stderr=stderr,
        env=env
    )
    
    if verbose:
        for line in process.stdout:
            print(line.decode().strip())
    
    process.wait()
    return process.returncode