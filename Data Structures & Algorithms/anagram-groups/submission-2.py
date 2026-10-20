class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in strs:
            d["".join(sorted(i))] = []

        for i in strs:
            d["".join(sorted(i))].append(i)

        return list(d.values())      
            

