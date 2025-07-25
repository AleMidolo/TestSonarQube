def subprocess_run_helper(func, *args, timeout, extra_env=None):
    """
    एक सब-प्रोसेस में एक फ़ंक्शन चलाएँ।

    पैरामीटर (Parameters)
    ---------------------
    func : function
        वह फ़ंक्शन जिसे चलाना है। यह किसी ऐसे मॉड्यूल में होना चाहिए जिसे आयात (import) किया जा सके।
    *args : str
        कोई भी अतिरिक्त कमांड लाइन तर्क जो ``subprocess.run`` के पहले तर्क में पास किए जाने हैं।
    extra_env : dict[str, str]
        सब-प्रोसेस के लिए सेट किए जाने वाले कोई भी अतिरिक्त पर्यावरण वेरिएबल।
    """
    import subprocess
    import os

    # Prepare the environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Prepare the command to run
    command = [func] + list(args)

    # Run the subprocess
    result = subprocess.run(command, env=env, timeout=timeout)

    return result