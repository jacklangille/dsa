class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        charSet = set()
        s = s.lower()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

s =  'ThisIsMyString'
sol = Solution()
print(sol.lengthOfLongestSubstring(s))



