class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # hold 2 nums in stack.
        # pop when an operator is noticed
        # perform operation and push into stack
        # repeat
        stack=[]
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            else:
                num1=stack.pop()
                num2=stack.pop()
                if token=="+":
                    stack.append(int(num1)+int(num2))
                elif token=="-":
                    stack.append(int(num2)-int(num1))
                elif token=="*":
                    stack.append(int(num1)*int(num2))
                elif token=="/":
                    stack.append(int(num2)/int(num1))
        return int(stack[-1])
                    
            