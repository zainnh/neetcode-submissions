class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for words in strs:
            seen = {}
            for letters in words:
                if letters in seen:
                    seen[letters] += 1
                else:
                    seen[letters] = 1

            key = tuple(sorted(seen.items()))

            if key in groups:
                groups[key].append(words)
            else:
                groups[key] = [words]
        return list(groups.values())
                
            
                
            




        