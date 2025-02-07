class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a','e','i','o','u','A','E','I','O','U']
        left = 0
        right = len(s) - 1
        positions = []
        vows = []

        for i, c in enumerate(s):
            if c in v:
                positions.append(i)
                vows.append(c)
        
        vows.reverse()

        output = list(s)
        for x in zip(positions, vows):
            output[x[0]] = x[1]
        
        return "".join(output)



s: str = "HelloMyNameIsJack"

sol: Solution = Solution()

print(sol.reverseVowels(s))


