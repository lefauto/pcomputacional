class Solution(object):
    def findWordsContaining(self, words, x):
        output =[]
        for word in words:
            if x in word:
                output.append(words.index(word))
        return output
