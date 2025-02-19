import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;

public static List<ThreadSnapshot> parseFromFileWithTimeRange(File file, List<ProfileAnalyzeTimeRange> timeRanges) throws IOException {
    List<ThreadSnapshot> snapshots = new ArrayList<>();
    List<String> lines = Files.readAllLines(file.toPath());

    for (String line : lines) {
        ThreadSnapshot snapshot = parseLineToThreadSnapshot(line);
        if (isWithinTimeRange(snapshot, timeRanges)) {
            snapshots.add(snapshot);
        }
    }

    return snapshots;
}

private static ThreadSnapshot parseLineToThreadSnapshot(String line) {
    // Implement the logic to parse a line into a ThreadSnapshot object
    // This is a placeholder implementation
    return new ThreadSnapshot(); // Replace with actual parsing logic
}

private static boolean isWithinTimeRange(ThreadSnapshot snapshot, List<ProfileAnalyzeTimeRange> timeRanges) {
    // Implement the logic to check if the snapshot's time is within the specified ranges
    // This is a placeholder implementation
    return true; // Replace with actual time range checking logic
}