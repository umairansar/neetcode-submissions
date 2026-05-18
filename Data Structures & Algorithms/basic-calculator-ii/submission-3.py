class Solution:
    def calculate(self, s: str) -> int:
        ops = set({"+", "*", "-", "/"})
        s = s.replace(" ", "")
        stack = []
        n = len(s)
        i = 0
        op = "+"
        num = 0
        while i < n:
            # print(s[i], op, num, stack)
            if s[i] not in ops:
                num = num * 10 + int(s[i])
                if i == n-1:
                    match op:
                        case "/":
                            old = stack.pop()
                            stack.append(int(old / num))
                        case "*":
                            old = stack.pop()
                            # print(old, num)
                            stack.append(int(old * num))
                        case "+":
                            stack.append(num)
                        case "-":
                            stack.append(-num)
            else:
                match op:
                    case "/":
                        old = stack.pop()
                        stack.append(int(old / num))
                    case "*":
                        old = stack.pop()
                        # print(old, num)
                        stack.append(int(old * num))
                    case "+":
                        stack.append(num)
                    case "-":
                        stack.append(-num)
                op = s[i]
                num = 0
            i += 1
        return sum(stack)