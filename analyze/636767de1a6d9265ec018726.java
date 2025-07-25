import java.util.ArrayList;
import java.util.List;

public class SequenceRangeBuilder {

    /** 
     * costruisce l'intervallo di sequenze per lo snapshot dei profili correnti
     */
    public List<SequenceRange> buildSequenceRanges() {
        List<SequenceRange> sequenceRanges = new ArrayList<>();
        
        // Example logic to create sequence ranges
        // This should be replaced with actual logic to build the ranges
        for (int i = 0; i < 10; i++) {
            SequenceRange range = new SequenceRange(i * 10, (i + 1) * 10 - 1);
            sequenceRanges.add(range);
        }
        
        return sequenceRanges;
    }

    public static class SequenceRange {
        private int start;
        private int end;

        public SequenceRange(int start, int end) {
            this.start = start;
            this.end = end;
        }

        public int getStart() {
            return start;
        }

        public int getEnd() {
            return end;
        }

        @Override
        public String toString() {
            return "SequenceRange{" +
                    "start=" + start +
                    ", end=" + end +
                    '}';
        }
    }

    public static void main(String[] args) {
        SequenceRangeBuilder builder = new SequenceRangeBuilder();
        List<SequenceRange> ranges = builder.buildSequenceRanges();
        for (SequenceRange range : ranges) {
            System.out.println(range);
        }
    }
}