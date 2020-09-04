

class stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None]* self.__max_size
        self.__top = -1

    def push(self, data):
        if self.isFull():
            return "stack is full"
        else:
            self.__top += 1
            self.__elements[self.__top] = data
            return "Pushed"

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data


    def isFull(self):
        if self.__max_size - 1 == self.__top:
            return True
        return False
    
    def isEmpty(self):
        if -1 == self.__top:
            return True
        return False

    def __str__(self):
        i = self.__top
        msg = ''
        while i >= 0:
            msg += str(self.__elements[i]) + " "
            i -= 1
        return msg
    
stack = stack(5)

print(stack.pop())
print(stack.push(5))
print(stack.push(5))
print(stack.push(5))
print(stack.push(5))
print(stack.push(5))
print(stack.push(5))

print(stack)