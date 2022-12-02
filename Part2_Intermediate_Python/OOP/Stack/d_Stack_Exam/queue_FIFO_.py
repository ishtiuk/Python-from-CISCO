
class QueueError(IndexError):  # Choose base class for the new exception.
    pass



class Queue:
    def __init__(self):
        self.__queue = []
        self.__dhanda =5


    def put(self, elem):
        self.__queue.append(elem)


    def get(self):
        
        if len(self.__queue) > 0:
            val = self.__queue[0]
            del self.__queue[0]
            return val

        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)


try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")

print(que.__dict__)