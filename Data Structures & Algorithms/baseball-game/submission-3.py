class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        
        for item in operations:
            if item == "D":
                stack.append(2 * stack[-1])
            elif item == "+":
                stack.append(stack[-1] + stack[-2])
            elif item == "C":
                stack.pop()
            else: 
                stack.append(int(item))

        return sum(stack)

            
        