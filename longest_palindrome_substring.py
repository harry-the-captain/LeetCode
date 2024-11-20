class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        rLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > rLen:
                    res = s[l : r + 1]
                    rLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > rLen:
                    res = s[l : r + 1]
                    rLen = r - l + 1
                l -= 1
                r += 1

        return res
    
    print(longestPalindrome(1,"babad"))
