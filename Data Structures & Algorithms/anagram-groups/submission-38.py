class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #edge case
        if len(strs) == 1:
            return [[strs[0]]]

        anagram_map = {}
        for string in strs: #'tops'
            word = "".join(sorted(string)) #'opst'
            if word not in anagram_map:
                anagram_map[word] = [string]
            else:
                anagram_map[word].append(string)
        return list(anagram_map.values())


        