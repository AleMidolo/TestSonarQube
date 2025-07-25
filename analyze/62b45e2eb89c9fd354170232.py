def next_version(version):
    # Split version into parts by dot
    parts = version.split('.')
    
    # Convert parts to integers
    nums = [int(x) for x in parts]
    
    # Start from rightmost digit
    i = len(nums) - 1
    
    while i >= 0:
        # If current digit is 9, set to 0 and continue to next digit
        if nums[i] == 9:
            nums[i] = 0
            i -= 1
        else:
            # Otherwise increment current digit and break
            nums[i] += 1
            break
            
    # If we ran out of digits to increment, add a 1 at the start
    if i < 0:
        nums.insert(0, 1)
        
    # Convert back to strings preserving original zero padding
    result = []
    for i in range(len(nums)):
        # Get original part to check if it had zero padding
        orig = parts[i] if i < len(parts) else ''
        if orig.startswith('0') and len(orig) > 1:
            # Preserve zero padding
            result.append(str(nums[i]).zfill(len(orig)))
        else:
            result.append(str(nums[i]))
            
    return '.'.join(result)