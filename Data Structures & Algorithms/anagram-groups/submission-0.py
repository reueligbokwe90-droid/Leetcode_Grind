class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        phrases = defaultdict(list)
        for words in strs:
            #for anagrams they have to contain all the letters so we use a sorted tuple  and then append
            key = tuple(sorted(words))
            # for a specific key of letters, the words are grouped
            phrases[key].append(words)
        return list(phrases.values())