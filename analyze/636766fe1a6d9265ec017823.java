public int addConstantNameAndType(final String name, final String descriptor) {
    // Assuming there's a constant pool implemented as a List or Map
    for (ConstantNameAndTypeInfo constant : constantPool) {
        if (constant.getName().equals(name) && constant.getDescriptor().equals(descriptor)) {
            return constant.getIndex(); // Return existing symbol index
        }
    }
    
    // Create a new ConstantNameAndTypeInfo if not found
    ConstantNameAndTypeInfo newConstant = new ConstantNameAndTypeInfo(name, descriptor);
    constantPool.add(newConstant);
    return newConstant.getIndex(); // Return the index of the new constant
}