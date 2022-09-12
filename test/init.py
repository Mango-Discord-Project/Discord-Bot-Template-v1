class Test:
    def __init__(self) -> None:
        self.value = 10
        self.__dict__ |= self.init()
        
    def init(self):
        def foo(value=(lambda: self.value)):
            print(value() + 10)
        def bar(value=(lambda: self.value*10)):
            print(value())
        return locals()

test = Test()
test.foo(); test.bar()
test.value = 100
test.foo(); test.bar()