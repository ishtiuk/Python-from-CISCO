
class Stack:
    def __init__(self):          # Simple Constructor...                
        self.__stack_list = []        # Private Attribute  | Encapsulation concepts ;)


    def push(self, item):
        self.__stack_list.append(item)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]

        return val


class AddingStack(Stack): 
                                                 # this class will be able to do the same thing of it's superclass, and moreover will be able to keep "sum" of the all Stack elements.... ;)😎
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        

    def get_sum(self):
        return self.__sum


    def push(self, item):
        self.__sum += item
        Stack.push(self, item)


    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val

        return val



obj_child = AddingStack()

for i in range(5):
    obj_child.push(i)

print("sum of all elements:", obj_child.get_sum())


for j in range(5):
    print(obj_child.pop())