import javax.swing.*;
import java.awt.*;

public class TableRowSelector {

    /** 
     * Seleziona la riga specificata nella JTable specificata e scorre lo JScrollPane specificato fino alla riga appena selezionata. 
     * Più importante, la chiamata a repaint() è ritardata abbastanza a lungo da permettere alla tabella di dipingere correttamente la riga appena selezionata, 
     * che potrebbe essere fuori dallo schermo.
     * @param row deve appartenere allo JScrollPane specificato
     * @param table deve appartenere allo JScrollPane specificato
     * @param pane deve appartenere allo JScrollPane specificato
     */
    public static void selectRow(int row, JTable table, JScrollPane pane) {
        if (table == null || pane == null || row < 0 || row >= table.getRowCount()) {
            throw new IllegalArgumentException("Invalid parameters");
        }

        // Seleziona la riga
        table.setRowSelectionInterval(row, row);
        
        // Scorre lo JScrollPane fino alla riga selezionata
        Rectangle rect = table.getCellRect(row, 0, true);
        table.scrollRectToVisible(rect);
        
        // Ritarda la chiamata a repaint
        SwingUtilities.invokeLater(() -> {
            table.repaint();
        });
    }

    public static void main(String[] args) {
        // Esempio di utilizzo
        JFrame frame = new JFrame("Table Row Selector Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        String[] columnNames = {"Column 1", "Column 2"};
        Object[][] data = {
            {"Row 1", "Data 1"},
            {"Row 2", "Data 2"},
            {"Row 3", "Data 3"},
            {"Row 4", "Data 4"},
            {"Row 5", "Data 5"},
        };
        JTable table = new JTable(data, columnNames);
        JScrollPane pane = new JScrollPane(table);
        frame.add(pane, BorderLayout.CENTER);
        frame.setSize(300, 200);
        frame.setVisible(true);

        // Seleziona la riga 2 dopo 1 secondo
        Timer timer = new Timer(1000, e -> selectRow(2, table, pane));
        timer.setRepeats(false);
        timer.start();
    }
}