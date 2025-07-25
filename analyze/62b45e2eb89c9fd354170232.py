def next_version(version):
    # Split version into parts
    parts = version.split('.')
    
    # Convert to integers
    nums = [int(x) for x in parts]
    
    # Start from rightmost digit
    i = len(nums) - 1
    
    while i >= 0:
        # If current digit is 9, set to 0 and continue carrying
        if nums[i] == 9:
            nums[i] = 0
            i -= 1
        # Otherwise increment digit and break
        else:
            nums[i] += 1
            break
            
    # If we carried through all digits, add new digit 1 at start
    if i < 0:
        nums.insert(0, 1)
        
    # Convert back to strings, preserving leading zeros
    result = []
    for i, num in enumerate(nums):
        # Keep leading zeros if original had them
        if parts[i].startswith('0') and num != 0:
            result.append('0' + str(num))
        elif parts[i].startswith('0'):
            result.append('0' + str(num))
        else:
            result.append(str(num))
            
    return '.'.join(result)