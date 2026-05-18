class Solution:
    def calculate(self, s: str) -> int:
        ops = set({"+", "*", "-", "/"})
        s = s.replace(" ", "")
        stack = []
        n = len(s)
        i = 0
        op = "+"
        num = 0

        def apply_op():
            match op:
                case "/":
                    stack.append(int(stack.pop() / num))
                case "*":
                    stack.append(stack.pop() * num)
                case "+":
                    stack.append(num)
                case "-":
                    stack.append(-num)

        while i < n:
            if s[i] not in ops:
                num = num * 10 + int(s[i])
                if i == n-1:
                    apply_op()
            else:
                apply_op()
                op = s[i]
                num = 0
            i += 1
        return sum(stack)