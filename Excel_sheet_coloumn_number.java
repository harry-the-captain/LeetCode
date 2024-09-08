class Solution {
    public int titleToNumber(String columnTitle) {
        
        int result = 0;
        int n = columnTitle.length();
        for(int i=0; i<n; i++)
        {
            int a = columnTitle.charAt(i) - 'A' + 1;
            result = result * 26 + a;
        }
        return result;
    }
}
