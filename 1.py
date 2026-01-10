class Solution():
    def twoSum(nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complementary = target - num
            
            if complementary in seen:
                print(seen[complementary])
                return [seen[complementary], i]
            else:
                seen[num] = i
      
                

            
        