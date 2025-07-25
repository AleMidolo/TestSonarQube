public class Request {
    private String content;

    public Request(String content) {
        this.content = content;
    }

    /** 
     * Recupera la lunghezza del contenuto della richiesta.
     * @return La lunghezza del contenuto della richiesta.
     * @since 1.3
     */
    public long contentLength() {
        return content != null ? content.length() : 0;
    }

    public static void main(String[] args) {
        Request request = new Request("Hello, World!");
        System.out.println("Content Length: " + request.contentLength());
    }
}