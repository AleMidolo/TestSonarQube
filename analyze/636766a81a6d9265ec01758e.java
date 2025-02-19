public static int nextPrime(int desiredCapacity) {
    if (desiredCapacity <= 1) {
        return 2;
    }

    int upperLimit = desiredCapacity;
    if (desiredCapacity >= 1000) {
        upperLimit = (int) (desiredCapacity * 1.11);
    }

    for (int i = desiredCapacity; i <= upperLimit; i++) {
        if (isPrime(i)) {
            return i;
        }
    }
    return upperLimit; // Fallback, should not reach here for valid input
}

private static boolean isPrime(int number) {
    if (number <= 1) {
        return false;
    }
    if (number <= 3) {
        return true;
    }
    if (number % 2 == 0 || number % 3 == 0) {
        return false;
    }
    for (int i = 5; i * i <= number; i += 6) {
        if (number % i == 0 || number % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}