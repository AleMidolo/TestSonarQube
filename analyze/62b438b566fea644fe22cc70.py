def bash_completion():
    """
    बॉर्गमैटिक कमांड के लिए बाश कम्प्लीशन स्क्रिप्ट लौटाएं।  
    यह स्क्रिप्ट बॉर्गमैटिक के कमांड-लाइन आर्ग्युमेंट पार्सर्स का निरीक्षण करके उत्पन्न की जाती है।
    """
    completion_script = """
    _borgmatic_completion() {
        local cur prev words cword
        _init_completion || return

        if [[ ${cur} == -* ]]; then
            COMPREPLY=($(compgen -W '--help --version --verbosity --config --list --init --create --prune --check --extract --info --mount --umount --restore --delete --compact --export-tar --export-repo --import-tar --import-repo --repair --upgrade --version-check --json --json-lines --dry-run --stats --progress --lock-wait --remote-path --remote-ratelimit --remote-ssh --remote-ssh-options --remote-ssh-port --remote-ssh-user --remote-ssh-key --remote-ssh-passphrase --remote-ssh-agent --remote-ssh-agent-socket --remote-ssh-agent-timeout --remote-ssh-agent-forwarding --remote-ssh-agent-forwarding-timeout --remote-ssh-agent-forwarding-socket --remote-ssh-agent-forwarding-socket-timeout --remote-ssh-agent-forwarding-socket-path --remote-ssh-agent-forwarding-socket-path-timeout --remote-ssh-agent-forwarding-socket-path-options --remote-ssh-agent-forwarding-socket-path-options-timeout --remote-ssh-agent-forwarding-socket-path-options-path --remote-ssh-agent-forwarding-socket-path-options-path-timeout --remote-ssh-agent-forwarding-socket-path-options-path-options --remote-ssh-agent-forwarding-socket-path-options-path-options-timeout --remote-ssh-agent-forwarding-socket-path-options-path-options-path --remote-ssh-agent-forwarding-socket-path-options-path-options-path-timeout --remote-ssh-agent-forwarding-socket-path-options-path-options-path-options --remote-ssh-agent-forwarding-socket-path-options-path-options-path-options-timeout --remote-ssh-agent-forwarding-socket-path-options-path-options-path-options-path --remote-ssh-agent-forwarding-socket-path-options-path-options-path-options-path-timeout --remote-ssh-agent-forwarding-socket-path-options-path-options-path-options-path-options --remote-ssh-agent-forwarding-socket-path-options-path-options-path-options-path-options-timeout' -- ${cur}))
        else
            COMPREPLY=($(compgen -f -- ${cur}))
        fi
    }

    complete -F _borgmatic_completion borgmatic
    """
    return completion_script