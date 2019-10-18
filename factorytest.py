class Definitions():
    def __init__(self):
        self.test = 1
        
    def get_test(self):
        return self.test

factory = {
    "1" : Definitions
}

testClass = factory["1"]
testObject = testClass()

print(testObject.get_test())
