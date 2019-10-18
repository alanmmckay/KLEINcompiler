##This is the basic rundown of how the semantic action
##portion of the parse algorithm will create the node objects.

class anASTNode():
    def __init__(self, stack):
        self.test = stack.pop()
        
    def get_test(self):
        return self.test

factory = {
    1 : anASTNode
}

stack = [1,2,"three",4,(4+1), 6]


while(len(stack) > 0):
    testClass = factory[1]
    testObject = testClass(stack)
    print(testObject.get_test())
    print(stack)
