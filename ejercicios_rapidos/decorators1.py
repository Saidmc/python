def Decorator(func):
    def Inner():
        print('='*7)
        func()
        print('='*14)
    return Inner

@Decorator
def sayHello():
    print('Hello')



decorated = Decorator(sayHello)
decorated()
sayHello()