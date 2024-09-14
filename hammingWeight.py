class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)   # bin() method used to convert integer to binary 
        count = 0

        for i in binary[2:]:   # binary is string so, i used binary[2:]
            if i == '1':
                count += 1

        return count
        
