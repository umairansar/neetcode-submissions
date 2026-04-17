class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i, n = 0, len(tokens)
        stack = []
        ops = "+*/-"
        while i < n:
            if tokens[i] in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                match tokens[i]:
                    case "/":
                        result = int(a / b)
                    case "+":
                        result = a + b
                    case "*":
                        result = a * b
                    case "-":
                        result = a - b
                stack.append(result)
            else:
                stack.append(tokens[i])
            i += 1
        return int(stack.pop())