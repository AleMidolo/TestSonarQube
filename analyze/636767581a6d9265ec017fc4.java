public static long fattoriale(int n) {
    if (n < 0) {
        throw new IllegalArgumentException("Il numero deve essere non negativo.");
    }
    long risultato = 1;
    for (int i = 2; i <= n; i++) {
        risultato *= i;
    }
    return risultato;
}