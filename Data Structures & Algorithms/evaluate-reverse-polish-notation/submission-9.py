class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0
        if len(tokens)<2:
            return int(tokens[0])
        for token in tokens:
            if token not in ['+', "*", "-", "/"]:
                stack.append(token)
            elif token == "+":
                    answer = int(stack.pop(-1))
                    answer+=int(stack.pop(-1))
                    stack.append(answer)
            elif token == "-":
                    answer = int(stack.pop(-1))
                    answer=int(stack.pop(-1))-answer
                    stack.append(answer)
            elif token == "*":
                    answer = int(stack.pop(-1))
                    answer*=int(stack.pop(-1))
                    stack.append(answer)
            elif token == "/":
                    answer = int(stack.pop(-1))
                    answer=int(stack.pop(-1))/answer
                    stack.append(answer)
        return int(stack[-1])
                