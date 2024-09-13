class Solution {
    public int divide(int dividend, int divisor) {
       if (divisor == 1) return dividend;

        long result = 0;
        long sign = 1;

        if ((dividend < 0 && divisor >= 0) || (dividend >= 0 && divisor < 0)) {
            sign = -1; // Different signs => result will be negative
        }

        long dd = Math.abs((long) dividend); // Absolute value of dividend
        long dr = Math.abs((long) divisor);  // Absolute value of divisor

        for (int i = 30; i >= 0; i--) {
            if (dd >= (dr << i)) {
                result += (1 << i); // Add 2^i to the result
                dd -= (dr << i);    // Subtract (divisor * 2^i) from dividend
            }
        }

        return (int) (result * sign);
    }
}
