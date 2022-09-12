class Test:
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, exc_type, exc_value, exc_trackback):
        print("exit")

def foo():
    with Test() as test:
        return test

foo()