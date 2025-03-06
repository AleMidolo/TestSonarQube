def bash_completion():
    """
    बॉर्गमैटिक कमांड के लिए बाश कम्प्लीशन स्क्रिप्ट लौटाएं।  
    यह स्क्रिप्ट बॉर्गमैटिक के कमांड-लाइन आर्ग्युमेंट पार्सर्स का निरीक्षण करके उत्पन्न की जाती है।
    """
    bash_script = """
    _borgmatic_completion() {
        local cur prev words cword
        _init_completion || return

        if [[ ${cur} == -* ]]; then
            COMPREPLY=($(compgen -W "--help --version --verbosity --config --list --create --prune --check --extract --info --init --stats --umask --lock-wait --borg-version --borg-help --borg-debug --borg-info --borg-warning --borg-error --borg-critical --borg-quiet --borg-verbose --borg-progress --borg-json --borg-log --borg-lock --borg-cache --borg-security-dir --borg-encryption --borg-repository --borg-archive --borg-prefix --borg-pattern --borg-exclude --borg-exclude-from --borg-exclude-caches --borg-exclude-if-present --borg-keep-tag --borg-keep-within --borg-keep-last --borg-keep-hourly --borg-keep-daily --borg-keep-weekly --borg-keep-monthly --borg-keep-yearly --borg-keep-minutely --borg-keep-secondly --borg-keep-interval --borg-keep-tag-file --borg-keep-within-file --borg-keep-last-file --borg-keep-hourly-file --borg-keep-daily-file --borg-keep-weekly-file --borg-keep-monthly-file --borg-keep-yearly-file --borg-keep-minutely-file --borg-keep-secondly-file --borg-keep-interval-file --borg-keep-tag-dir --borg-keep-within-dir --borg-keep-last-dir --borg-keep-hourly-dir --borg-keep-daily-dir --borg-keep-weekly-dir --borg-keep-monthly-dir --borg-keep-yearly-dir --borg-keep-minutely-dir --borg-keep-secondly-dir --borg-keep-interval-dir --borg-keep-tag-regex --borg-keep-within-regex --borg-keep-last-regex --borg-keep-hourly-regex --borg-keep-daily-regex --borg-keep-weekly-regex --borg-keep-monthly-regex --borg-keep-yearly-regex --borg-keep-minutely-regex --borg-keep-secondly-regex --borg-keep-interval-regex --borg-keep-tag-glob --borg-keep-within-glob --borg-keep-last-glob --borg-keep-hourly-glob --borg-keep-daily-glob --borg-keep-weekly-glob --borg-keep-monthly-glob --borg-keep-yearly-glob --borg-keep-minutely-glob --borg-keep-secondly-glob --borg-keep-interval-glob" -- ${cur}))
        else
            COMPREPLY=($(compgen -f -- ${cur}))
        fi
    }
    complete -F _borgmatic_completion borgmatic
    """
    return bash_script