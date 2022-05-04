# -----------------------------------------------------------------------------
#  Attempt: #1                start of solution
# -----------------------------------------------------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        
        for string in strs:
            count = [0]*26
            
            for c in string:
                count[ord(c) - ord('a')] +=1
                
            hashmap[tuple(count)].append(string)
        return hashmap.values()