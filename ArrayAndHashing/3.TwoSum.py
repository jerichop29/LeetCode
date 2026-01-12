class Solution:
    def twoSum(nums, target):
        seen = {}
        
        for i, num in enumerate(nums):
            complementary = target - num
            if complementary not in seen:
                seen[num] = i
            else:
                print(seen)
                return [seen[complementary], i]

#print(Solution.twoSum([3,4,5,6], 7)) [0,1]