from enum import *

class Definitions():
    def __init__(self, stack):
        self.test = stack.pop()
        
    def get_test(self):
        return self.test

factory = {
    "1" : Definitions
}

stack = [1]

testClass = factory["1"]
testObject = testClass(stack)


print(testObject.get_test())

print(stack)
