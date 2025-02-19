public void abbreviate(final int nameStart, final StringBuffer buf) {
    String name = "ExampleName"; // Replace with the actual name to abbreviate
    if (nameStart < 0 || nameStart >= name.length()) {
        throw new IllegalArgumentException("Invalid nameStart index");
    }
    
    String abbreviation = name.substring(nameStart, nameStart + 1) + ".";
    buf.append(abbreviation);
}