class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:  
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        pref = [0]
        curr = 0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                curr += 1
            pref.append(curr)

        print(pref)
        res = []
        for li, ri in queries:
            res.append(pref[ri + 1] - pref[li])
        
        return res