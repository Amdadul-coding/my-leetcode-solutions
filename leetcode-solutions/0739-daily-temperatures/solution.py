class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        resultDay = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, idx = stack.pop()
                resultDay[idx] = i - idx
            stack.append([t,i])
        return resultDay
