@Override 
public String readString() throws IOException {
    StringBuilder stringBuilder = new StringBuilder();
    int character;
    while ((character = read()) != -1) {
        if (character == '\n') {
            break;
        }
        stringBuilder.append((char) character);
    }
    return stringBuilder.toString();
}