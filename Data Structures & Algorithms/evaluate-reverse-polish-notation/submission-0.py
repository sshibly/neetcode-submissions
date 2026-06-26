class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                # int() converts to int and rounds to 0
                stack.append(int(num1 / num2))
            else:
                stack.append(int(c))
        
        return stack.pop()

        # time complexity: O(n)
        # space complexity: O(n)

        

        