package moom.math.exercises.service;

import org.springframework.stereotype.Service;

public class EuclideanDivisionNaive {

    public static void main(String[] args) {
        long dividend = -1687, divisor = 11;
        Solution solution = longDivision(dividend, divisor);

        System.out.println("quotient  = " + solution.quotient());
        System.out.println("remainder = " + solution.remainder());
        System.out.println("dividend  = " + dividend
                + " = " + solution.quotient() + " * " + divisor
                + " + " + solution.remainder());
    }

    public static Solution longDivision(long dividend, long divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            throw new RuntimeException(); // TODO include msg
        }
        if (divisor == 0) throw new RuntimeException(); // TODO include msg

        boolean isNegative = (dividend < 0) ^ (divisor < 0);
        long longDividend = Math.abs((long) dividend);
        long longDivisor = Math.abs((long) divisor);

        int quotient = 0;
        while (longDividend >= longDivisor) {
            long temp = longDivisor;
            long multiple = 1;

            while (longDividend >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }

            longDividend -= temp;
            quotient += multiple;
        }

        int qq = isNegative ? -quotient : quotient;
        return new Solution(qq, longDividend);
    }

    private record Solution(long quotient, long remainder) {}

}