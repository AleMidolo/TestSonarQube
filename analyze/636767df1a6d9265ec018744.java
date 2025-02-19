protected List<TimeRange> buildTimeRanges(long start, long end) {
    List<TimeRange> timeRanges = new ArrayList<>();
    long fetchDataDuration = FETCH_DATA_DURATION; // Assuming FETCH_DATA_DURATION is defined elsewhere

    // Ensure start and end are within the allowed duration
    while (start < end) {
        long rangeEnd = Math.min(start + fetchDataDuration, end);
        timeRanges.add(new TimeRange(start, rangeEnd));
        start = rangeEnd; // Move to the next range
    }

    return timeRanges;
}