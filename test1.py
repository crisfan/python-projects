class A(object):
    def show(self):
        print 'aa'


class B(A):
    pass

b = B()
print isinstance(b, B)
print type(B)
print type(A)
