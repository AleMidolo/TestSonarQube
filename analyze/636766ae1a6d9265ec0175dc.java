public class HttpResponseChecker {

    private int statusCode;

    public HttpResponseChecker(int statusCode) {
        this.statusCode = statusCode;
    }

    /** 
     * Controlla se la risposta attuale è un Contenuto Parziale (codice HTTP 206)
     * @return vero se è contenuto parziale, falso altrimenti
     */
    public Boolean isPartialContentResponse() {
        return statusCode == 206;
    }

    public static void main(String[] args) {
        HttpResponseChecker responseChecker = new HttpResponseChecker(206);
        System.out.println("Is partial content response: " + responseChecker.isPartialContentResponse());
        
        HttpResponseChecker responseChecker2 = new HttpResponseChecker(200);
        System.out.println("Is partial content response: " + responseChecker2.isPartialContentResponse());
    }
}