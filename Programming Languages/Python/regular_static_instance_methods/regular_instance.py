class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


# can freely access attributes and other methods on the same object
# a lot of power to modify object's state
# can also modify class with .__class__ attribute

print(MyClass().method())
