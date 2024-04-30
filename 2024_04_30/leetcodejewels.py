class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        valor = 0
        for char in jewels:
            for char1 in stones:
                if char == char1:
                    valor += 1
        return valor