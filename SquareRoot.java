class Solution {
    public int mySqrt(int x) {

         if (x == 0 || x == 1)
         {
            return x;
        }

        int i = 1;
        long result = 1;

        while (result <= x) 
        {
            i++;
            result = (long) i * i;     // if i use int, it is showing error for huge numbers 
        }                                  
        return i - 1;
    }
}
