class Top(object):
    def __init__(self, **kwargs):
        pass  # Terminate the constructor call chain

class A(Top):
    def __init__(self, **kwargs):
        print("Making an A object")
        super().__init__(**kwargs)
        self.value_A = 0

class B(Top):
    def __init__(self, **kwargs):
        print("Making a B object")
        self.value_B = kwargs['val']
        kwargs.pop('val')    # Remove the parameter from the kwargs
        super().__init__(**kwargs)

class C(A, B):
    def __init__(self, **kwargs):
        print("Making a C object")
        super().__init__(**kwargs)
        self.value_C = 2

c_obj = C(val=5)  # Need to supply keyword argument here
print("===========")
print(c_obj.__dict__)
