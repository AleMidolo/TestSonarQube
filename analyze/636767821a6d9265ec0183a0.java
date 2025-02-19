protected static void deleteFile(String fileName) {
    java.io.File file = new java.io.File(fileName);
    if (file.exists()) {
        if (file.delete()) {
            System.out.println("File deleted successfully: " + fileName);
        } else {
            System.out.println("Failed to delete the file: " + fileName);
        }
    } else {
        System.out.println("File does not exist: " + fileName);
    }
}