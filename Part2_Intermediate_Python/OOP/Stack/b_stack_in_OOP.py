
class Stack:
    def __init__(self):          # Simple Constructor...
        print("Hi...")                  
        self.__stack = []        # Private Attribute  | Encapsulation concepts ;)


    def push(self, item):
        self.__stack.append(item)


    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]

        return val



stack_obj_1 = Stack()
stack_obj_2 = Stack()


stack_obj_1.push(4)
stack_obj_1.push(3)
stack_obj_1.push(2)
stack_obj_1.push(1)

print(stack_obj_1.pop())
print(stack_obj_1.pop())
print(stack_obj_1.pop())


stack_obj_2.push(stack_obj_1.pop())
print(stack_obj_2.pop())



try:
    print(len(stack_obj_1.stack))
except AttributeError as err:
    print(err)


# but I can access still now....... 😎😎
print(stack_obj_1._Stack__stack, "__saggaaaaaaaa........!!! ;D")              # ha ha .... saggaaaaaaaa........!!! ;D






















# obj = Stack()
# obj1 = Stack()

# stack_obj.push(8)
# print(stack_obj.list)

# print(stack_obj.list)

# print(obj.list)
# obj.push(9)
# print(obj.list)

# print(stack_obj.list)