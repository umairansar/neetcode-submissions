class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, reverse=True)
        times = [(target - p) / s for p, s in pairs]
        stack = []
        for i in range(len(times)):
            if not stack or (stack and stack[-1] < times[i]):
                stack.append(times[i])
        return len(stack)