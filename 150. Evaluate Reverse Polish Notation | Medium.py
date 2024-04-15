#https://leetcode.com/problems/evaluate-reverse-polish-notation/
#if else hell, but it works and beats 80% in speed
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tokensdone = None
        def makeint(a):
            return int(str(a).split('.')[0])
        while len(stack) != 1:
            for x in tokens:
                if tokensdone != True:
                    if x in "-+*/":
                        stack.append(x)
                    else:
                        stack.append(int(x))
                if len(stack) >= 3 and type(stack[-1]) == str:
                    if type(stack[-2]) == int and type(stack[-3]) == int and stack[-1] in "-+*/":
                        if stack[-1] == "/":
                            newval = stack[-3]/stack[-2]
                            if type(newval) == float:
                                newval = makeint(stack[-3]/stack[-2])
                            stack.pop(-1)
                            stack.pop(-1)
                            stack.pop(-1)
                            stack.append(newval)
                            continue
                        if stack[-1] == "*":
                            newval = stack[-3]*stack[-2]
                            if type(newval) == float:
                                newval = makeint(stack[-3]*stack[-2])
                            stack.pop(-1)
                            stack.pop(-1)
                            stack.pop(-1)
                            stack.append(newval)
                            continue
                        if stack[-1] == "-":
                            newval = stack[-3]-stack[-2]
                            stack.pop(-1)
                            stack.pop(-1)
                            stack.pop(-1)
                            stack.append(newval)
                            continue
                        if stack[-1] == "+":
                            newval = stack[-3]+stack[-2]
                            stack.pop(-1)
                            stack.pop(-1)
                            stack.pop(-1)
                            stack.append(newval)
                            continue
            tokensdone = True
            return stack[0]
