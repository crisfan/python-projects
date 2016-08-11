# -*- coding:utf-8 -*-


class AddrBookEntry(object):
    def __init__(self, nm, ph):
        self.name = nm
        self.ph = ph
        print 'Creat instance for:', self.name

    def updatePhone(self, newph):
        self.phone = newph
        print 'Updated phone # for:', self.name


class EmpleAddrBookEntry(AddrBookEntry):
    """类解释文档"""
    # 每个类没有定义自己的构造器,那么基类的构造器会被调用
    # 如果子类定义了自己的构造器,那么基类的构造器必须显式写出才会被执行.
    fool = 5

    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em
        print '添加邮箱'

    def updateEmail(self, newem):
        self.email = newem
        print 'Updated e-mail address for:', self.name

# 查看类属性
print dir(EmpleAddrBookEntry)
print EmpleAddrBookEntry.__dict__
print EmpleAddrBookEntry.__name__

# 类c所有父类构成的元组
print EmpleAddrBookEntry.__bases__

print EmpleAddrBookEntry.__class__
