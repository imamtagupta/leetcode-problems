
################################################
# 3016. Minimum Number of Pushes to Type Word II #
################################################

# leetcode link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)

        ans = 0
        for i, x in enumerate(sorted(cnt.values(), reverse=True)):
            ans += (i // 8 + 1) * x
        return ans