def size_to_bytes(size: str) -> int:
    size = size.strip().upper()
    units = {
        'B': 1,
        'K': 1000,
        'M': 1000000,
        'G': 1000000000,
        'T': 1000000000000,
    }
    
    for unit in units:
        if size.endswith(unit):
            number = size[:-1].strip()
            return int(float(number) * units[unit])
    
    return int(size)