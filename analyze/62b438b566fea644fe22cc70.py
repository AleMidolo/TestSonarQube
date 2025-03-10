def bash_completion():
    """
    बॉर्गमैटिक कमांड के लिए बाश कम्प्लीशन स्क्रिप्ट लौटाएं।  
    यह स्क्रिप्ट बॉर्गमैटिक के कमांड-लाइन आर्ग्युमेंट पार्सर्स का निरीक्षण करके उत्पन्न की जाती है।
    """
    script = """
    _borgmatic_completion() {
        local cur prev words cword
        _init_completion || return

        if [[ ${cur} == -* ]]; then
            COMPREPLY=($(compgen -W '--help --version --verbosity --config --list --create --prune --check --extract --info --init --upgrade --borg-version --override --json --dry-run --stats --progress --lock-wait --remote-path --one-file-system --exclude --exclude-from --keep-tag --keep-within --keep-last --keep-hourly --keep-daily --keep-weekly --keep-monthly --keep-yearly --prefix --glob-archives --match-archives --match-archives-glob --match-archives-regex --match-archives-tag --match-archives-tag-glob --match-archives-tag-regex --match-archives-tag-prefix --match-archives-tag-suffix --match-archives-tag-contains --match-archives-tag-exact --match-archives-tag-regex-contains --match-archives-tag-regex-exact --match-archives-tag-regex-prefix --match-archives-tag-regex-suffix --match-archives-tag-regex-contains --match-archives-tag-regex-exact --match-archives-tag-regex-prefix --match-archives-tag-regex-suffix --match-archives-tag-regex-contains --match-archives-tag-regex-exact --match-archives-tag-regex-prefix --match-archives-tag-regex-suffix --match-archives-tag-regex-contains --match-archives-tag-regex-exact --match-archives-tag-regex-prefix --match-archives-tag-regex-suffix --match-archives-tag-regex-contains --match-archives-tag-regex-exact --match-archives-tag-regex-prefix --match-archives-tag-regex-suffix --match-archives-tag-regex-contains --match-archives-tag-regex-exact --match-archives-tag-regex-prefix --match-archives-tag-regex-suffix' -- ${cur}))
        else
            COMPREPLY=($(compgen -f -- ${cur}))
        fi
    }

    complete -F _borgmatic_completion borgmatic
    """
    return script