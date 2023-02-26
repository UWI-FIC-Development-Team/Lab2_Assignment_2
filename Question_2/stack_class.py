class Stack:
        def __init__(self):
                self.lst = []
        
        def makeStack(self):return ('stack', self.lst)
        
        def contents(self, stk):return stk[1]
        
        def isStack(self, stk):
                return isinstance(stk, Stack)
                
        def push(self, item):
                self.lst.append(item)

        def pop(self):
                if not self.isStackEmpty():
                        return self.lst.pop()
                
        def isStackEmpty(self):
                return len(self.lst) == 0

        
        
        

stk =  Stack()

stk1 = stk.makeStack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.pop()

print(stk.contents(stk1))
# print(stk.isStack(stk))
