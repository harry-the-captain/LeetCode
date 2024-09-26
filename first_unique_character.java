class Solution {
    public int firstUniqChar(String s) {
        int[] arr = new int[100];
        char[] chars = s.toCharArray();
        for(char c: chars){
            arr[c-'a']++;
        }
        for(int i=0; i<chars.length; i++){
            if(arr[chars[i] - 'a'] == 1){
                return i;
            }
        }
        return -1;
    }
}
