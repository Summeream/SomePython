class C1(object):
    @staticmethod
    class C2(object):
        def __init__(self, val = 1):
            self.val = val
        def shout(self):
            print("Python世界第%d!"%self.val)
tmp = C1.C2(0)
print(type(tmp))    # 输出 : <class '__main__.C1.C2'>
tmp.shout()         # 输出 : Python世界第0

class C3:
    @staticmethod
    class C4:
        def __init__(self, val = 1):
            self.val = val
        def shout(self):
            print("Python世界第%d!"%self.val)
tmp1 = C3.C4()
print(type(tmp1))    # 输出 : <class '__main__.C1.C2'>
tmp1.shout()         # 输出 : Python世界第0