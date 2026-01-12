from collections import Counter
class Solution:
    def groupAnagrams(strs):
        list = []
        left = 0
        
        for right in range(1, len(strs)):
            subList = []
            if Counter(strs[left]) == Counter(strs[right]):
                subList.append(strs[right])

            
            print(subList)


                
print(Solution.groupAnagrams(["opts","tac","tops","cat","stop","pots"]))