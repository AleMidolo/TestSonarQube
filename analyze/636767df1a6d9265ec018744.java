import java.util.ArrayList;
import java.util.List;

public class TimeRangeBuilder {

    private static final long FETCH_DATA_DURATION = 3600000; // Example duration in milliseconds (1 hour)

    /**
     * Suddivide gli intervalli di tempo per garantire che l'orario di inizio e l'orario di fine siano inferiori a {@link #FETCH_DATA_DURATION}
     */
    protected List<TimeRange> buildTimeRanges(long start, long end) {
        List<TimeRange> timeRanges = new ArrayList<>();
        
        // Validate input
        if (start >= end) {
            return timeRanges; // Return empty list if start is not less than end
        }

        // Create time ranges
        long currentStart = start;
        while (currentStart < end) {
            long currentEnd = Math.min(currentStart + FETCH_DATA_DURATION, end);
            timeRanges.add(new TimeRange(currentStart, currentEnd));
            currentStart = currentEnd; // Move to the next range
        }

        return timeRanges;
    }

    // Inner class to represent a time range
    public static class TimeRange {
        private final long start;
        private final long end;

        public TimeRange(long start, long end) {
            this.start = start;
            this.end = end;
        }

        public long getStart() {
            return start;
        }

        public long getEnd() {
            return end;
        }

        @Override
        public String toString() {
            return "TimeRange{" +
                    "start=" + start +
                    ", end=" + end +
                    '}';
        }
    }

    public static void main(String[] args) {
        TimeRangeBuilder builder = new TimeRangeBuilder();
        List<TimeRange> ranges = builder.buildTimeRanges(0, 10000000); // Example usage
        for (TimeRange range : ranges) {
            System.out.println(range);
        }
    }
}