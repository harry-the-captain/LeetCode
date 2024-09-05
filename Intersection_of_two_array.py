class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = {}

        # Count the frequency of elements in nums1
        for num in nums1:
            list1[num] = list1.get(num, 0) + 1

        # Check if elements in nums2 are present in nums1 and add them to the result
        result = []
        for num in nums2:
            if num in list1 and list1[num] > 0:
                result.append(num)
                list1[num] -= 1

        return result
