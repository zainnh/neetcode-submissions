class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Main = {}

        for words in strs:

            count = [0] * 26

            for char in words:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)

            if key not in Main:
                Main[key] = []
            Main[key].append(words)
        
        return list(Main.values())