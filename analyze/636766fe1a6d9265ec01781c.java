public static Character toCharacterObject(final char ch) {
    if (ch >= 0 && ch <= 127) {
        return Character.valueOf(ch);
    }
    return new Character(ch);
}