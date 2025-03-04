def render(pieces, style):
    """
    Render the given version pieces into the requested style.
    """
    if style == 'pep440':
        # PEP 440 format: major.minor.micro[.devN]
        version = '.'.join(str(p) for p in pieces[:3])
        if len(pieces) > 3:
            version += '.dev' + str(pieces[3])
        return version
        
    elif style == 'semver':
        # Semantic versioning: major.minor.patch[-devN]
        version = '.'.join(str(p) for p in pieces[:3])
        if len(pieces) > 3:
            version += '-dev.' + str(pieces[3])
        return version
        
    elif style == 'git':
        # Git style: vMAJOR.MINOR.MICRO-devN
        version = 'v' + '.'.join(str(p) for p in pieces[:3])
        if len(pieces) > 3:
            version += '-dev.' + str(pieces[3])
        return version
        
    else:
        # Default to basic dot notation
        return '.'.join(str(p) for p in pieces)