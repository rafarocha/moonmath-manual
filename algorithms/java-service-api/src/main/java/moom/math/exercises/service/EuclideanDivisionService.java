package moom.math.exercises.service;

import org.springframework.stereotype.Service;

@Service
public class EuclideanDivisionService {

    public SolutionLongDivision longDivision(long dividend, long divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return null;
        }

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
        return new SolutionLongDivision(qq, longDividend);
    }

}