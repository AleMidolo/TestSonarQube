public class ArrayDetailAppender {

    /**
     * <p>Aggiunge al <code>toString</code> i dettagli di un array di <code>int</code>.</p>
     * @param buffer  il <code>StringBuffer</code> da popolare
     * @param fieldName  il nome del campo, tipicamente non utilizzato poiché già aggiunto
     * @param array  l'array da aggiungere al <code>toString</code>, non <code>null</code>
     */
    protected void appendDetail(StringBuffer buffer, String fieldName, int[] array) {
        if (array == null) {
            throw new IllegalArgumentException("Array cannot be null");
        }
        buffer.append(fieldName).append(": [");
        for (int i = 0; i < array.length; i++) {
            buffer.append(array[i]);
            if (i < array.length - 1) {
                buffer.append(", ");
            }
        }
        buffer.append("]");
    }

    public static void main(String[] args) {
        ArrayDetailAppender appender = new ArrayDetailAppender();
        StringBuffer buffer = new StringBuffer();
        int[] array = {1, 2, 3, 4, 5};
        appender.appendDetail(buffer, "myArray", array);
        System.out.println(buffer.toString());
    }
}