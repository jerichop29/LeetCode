from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        
        groups = defaultdict(list)

        for str in strs:
            counter = [0] * 26
            for c in str:
                counter[ord(c) - ord('a')] += 1
            groups[tuple(counter)].append(str)
            
        result = list(groups.values())
        result.sort(key=len)
        
        return result

s = Solution()
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))