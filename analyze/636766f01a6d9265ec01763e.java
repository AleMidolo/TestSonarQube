private static String javaCharset(String charset) {
    switch (charset.toLowerCase()) {
        case "utf-8":
            return "UTF-8";
        case "iso-8859-1":
            return "ISO-8859-1";
        case "us-ascii":
            return "US-ASCII";
        case "windows-1252":
            return "windows-1252";
        case "utf-16":
            return "UTF-16";
        case "utf-16be":
            return "UTF-16BE";
        case "utf-16le":
            return "UTF-16LE";
        // Add more mappings as needed
        default:
            return charset; // Return the original if no match is found
    }
}