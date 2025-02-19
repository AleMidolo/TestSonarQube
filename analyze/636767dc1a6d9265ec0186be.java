static long compressTimeBucket(long timeBucket, int dayStep) {
    // Convert the long timeBucket to a string to manipulate the date
    String timeBucketStr = Long.toString(timeBucket);
    
    // Extract the year, month, and day from the timeBucket
    int year = Integer.parseInt(timeBucketStr.substring(0, 4));
    int month = Integer.parseInt(timeBucketStr.substring(4, 6));
    int day = Integer.parseInt(timeBucketStr.substring(6, 8));
    
    // Calculate the day of the month that is the closest multiple of dayStep
    int dayOfMonth = (day / dayStep) * dayStep;
    if (day % dayStep >= dayStep / 2) {
        dayOfMonth += dayStep;
    }
    
    // Handle the case where the dayOfMonth exceeds the number of days in the month
    int daysInMonth = java.time.Month.of(month).length(java.time.Year.isLeap(year));
    if (dayOfMonth > daysInMonth) {
        dayOfMonth = daysInMonth;
    }
    
    // Format the new date back to long
    String formattedDate = String.format("%04d%02d%02d", year, month, dayOfMonth);
    return Long.parseLong(formattedDate);
}