class Solution:
    #O(n) time and space
    #stack is monotically decreasing
    #used to find next greater elem in array
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            curr = temperatures[i]
            while stack and curr >= temperatures[stack[-1]]:
                temp = stack.pop()
                res[temp] = stack[-1] - temp if stack else 0
            stack.append(i)
        while len(stack) > 1:
            temp = stack.pop()
            res[temp] = stack[-1] - temp
        return res