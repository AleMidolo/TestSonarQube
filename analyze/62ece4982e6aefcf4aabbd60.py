def size_to_bytes(size: str) -> int:
    units = {
        'K': 1000,
        'M': 1000000,
        'G': 1000000000,
        'T': 1000000000000,
        'P': 1000000000000000,
        'E': 1000000000000000000,
        'Ki': 1024,
        'Mi': 1048576,
        'Gi': 1073741824,
        'Ti': 1099511627776,
        'Pi': 1125899906842624,
        'Ei': 1152921504606846976
    }

    size = size.strip()
    
    # If just a number is provided with no units
    if size.isdigit():
        return int(size)
        
    # Extract the numeric part and unit
    for unit in sorted(units.keys(), key=len, reverse=True):
        if size.endswith(unit):
            try:
                number = float(size[:-len(unit)])
                return int(number * units[unit])
            except ValueError:
                raise ValueError(f"Invalid size format: {size}")
                
    raise ValueError(f"Invalid size format: {size}")