from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        result = sorted(list(counter.keys())[-1:-k-1:-1])
        return result

s = Solution()
print(s.topKFrequent([7,7], 1))