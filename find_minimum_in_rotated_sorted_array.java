class Solution {
    public int findMin(int[] nums) {

        int start = 0;
        int end = nums.length - 1;
        int minElement = Integer.MAX_VALUE;    // java built in function for maximum number

        while (start <= end) {     // execute loop untill start and end become equal
            int mid = (start + end) / 2;

           
            if (nums[start] <= nums[end]) {      // If the array is already sorted
                minElement = Math.min(minElement, nums[start]);
                break;
            }

           
            if (nums[start] <= nums[mid]) {       // Check which half is sorted
                
                minElement = Math.min(minElement, nums[start]);  // Left half is sorted
                start = mid + 1;  // Move to the right half
            } else {
               
                minElement = Math.min(minElement, nums[mid]);    // Right half is sorted
                end = mid - 1;  // Move to the left half
            }
        }

        return minElement;
    }
}
