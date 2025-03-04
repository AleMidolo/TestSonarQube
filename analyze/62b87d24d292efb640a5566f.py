def render(pieces, style):
    """
    Render the given version pieces into the requested style.
    """
    if style == 'pep440':
        # PEP 440 format: N.N[.N]+[{a|b|c|rc}N][.postN][.devN]
        version = '.'.join(str(p) for p in pieces[:3])
        if len(pieces) > 3:
            if pieces[3] == 'alpha':
                version += f'a{pieces[4]}'
            elif pieces[3] == 'beta':
                version += f'b{pieces[4]}'
            elif pieces[3] == 'candidate':
                version += f'rc{pieces[4]}'
            elif pieces[3] == 'final':
                if pieces[4] > 0:
                    version += f'.post{pieces[4]}'
        if len(pieces) > 5 and pieces[5] > 0:
            version += f'.dev{pieces[5]}'
        return version
        
    elif style == 'semver':
        # Semantic versioning: MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
        version = '.'.join(str(p) for p in pieces[:3])
        if len(pieces) > 3:
            if pieces[3] != 'final':
                version += f'-{pieces[3]}.{pieces[4]}'
        if len(pieces) > 5 and pieces[5] > 0:
            version += f'+{pieces[5]}'
        return version
        
    else:
        raise ValueError(f'Unknown version style: {style}')