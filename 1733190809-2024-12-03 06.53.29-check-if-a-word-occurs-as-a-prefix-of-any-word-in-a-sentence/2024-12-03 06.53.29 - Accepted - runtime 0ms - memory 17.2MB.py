class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return ([-2] + [
            i for i, word in enumerate(sentence.split(' '))
            if len(word) >= len(searchWord) and word[:len(searchWord)] == searchWord
        ])[:2][-1] + 1