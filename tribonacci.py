class Solution:
    def tribonacci(self, n: int) -> int:

        if n <= 1:
            return n
        t = [0]*(n+1)
        t[0] = 0
        t[1] = 1
        t[2] = 1

        for i in range(3, n+1):
            print(t)
            t[i] = t[i-1] + t[i-2] + t[i-3]

        return t[n]
