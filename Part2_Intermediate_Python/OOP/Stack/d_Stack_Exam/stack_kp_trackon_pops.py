
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]

        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__total_pushed = 0
        self.__total_popped = 0


    def get_counter(self):
        return f"total pushed: {self.__total_pushed}\ntotal popped: {self.__total_popped}"

    
    def push(self, item):
        self.__total_pushed += 1
        Stack.push(self, item)

    def pop(self):
        self.__total_popped += 1
        Stack.pop(self)



stk = CountingStack()

for i in range(100):
    stk.push(i)
    
for i in range(15):
    stk.pop()
    
print(stk.get_counter())
