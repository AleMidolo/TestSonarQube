import java.util.ArrayList;
import java.util.List;
import javafx.util.Pair;

public class SuffixSumCalculator {

    /** 
     * Calcola la somma dei suffissi di {@code bounds}. Restituisce la somma dei suffissi calcolata e la somma totale di tutti gli elementi nella lista {@code bounds}.
     * @param bounds lista di interi.
     * @return coppia calcolata di lista di somma suffisso e somma di tutti gli elementi.
     */
    private Pair<List<Integer>, Long> computeSuffixSum(List<Integer> bounds) {
        List<Integer> suffixSums = new ArrayList<>();
        long totalSum = 0;
        int n = bounds.size();

        for (int i = 0; i < n; i++) {
            totalSum += bounds.get(i);
        }

        int currentSuffixSum = 0;
        for (int i = n - 1; i >= 0; i--) {
            currentSuffixSum += bounds.get(i);
            suffixSums.add(currentSuffixSum);
        }

        // Reverse the suffix sums list to maintain the original order
        List<Integer> reversedSuffixSums = new ArrayList<>();
        for (int i = suffixSums.size() - 1; i >= 0; i--) {
            reversedSuffixSums.add(suffixSums.get(i));
        }

        return new Pair<>(reversedSuffixSums, totalSum);
    }
}