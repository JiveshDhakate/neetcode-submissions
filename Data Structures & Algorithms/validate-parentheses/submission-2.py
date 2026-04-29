class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if i in '({[':
                stk.append(i)
            elif stk and ((i==')' and stk[-1]=='(') or (i=='}' and stk[-1]=='{') or (i==']' and stk[-1]=='[')):
                stk.pop()
            else:
                return False
        return len(stk)==0
        