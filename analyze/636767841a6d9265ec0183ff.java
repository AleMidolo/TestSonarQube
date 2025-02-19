import javax.swing.JTable;
import javax.swing.JScrollPane;
import javax.swing.SwingUtilities;

public static void selectRow(int row, JTable table, JScrollPane pane) {
    if (table == null || pane == null) {
        throw new IllegalArgumentException("Table and JScrollPane cannot be null");
    }
    
    if (row < 0 || row >= table.getRowCount()) {
        throw new IndexOutOfBoundsException("Row index is out of bounds");
    }

    // Select the specified row
    table.setRowSelectionInterval(row, row);
    
    // Scroll to the selected row
    SwingUtilities.invokeLater(() -> {
        pane.getViewport().setViewPosition(table.getLocationAtIndex(row));
        table.repaint();
    });
}