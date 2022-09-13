class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = str(bin(x))[2:]
        y = str(bin(y))[2:]
        
        m_length = max(len(x), len(y))
        x = "".join((["0"] * (m_length - len(x))) + [x])
        y = "".join((["0"] * (m_length - len(y))) + [y])
        
        cnt = 0
        for i in range(m_length):
            if x[i] != y[i]:
                cnt += 1
        return cnt
            