class A:
    def getA(self, a):
        self.a = a
    def setA(self):
        print("A :", self.a)
class B(A):
    def getB(self, b):
        self.b = b
    def setB(self):
        print("B :", self.b)
class C(A):
    def getC(self, c):
        self.c = c
    def setC(self):
        print("C :", self.c)
class D(B, C):
    def getD(self, d):
        self.d = d
    def setD(self):
        print("D :", self.d)


d1 = D()
d1.getA(10)
d1.setA()
d1.getB(20)
d1.setB()
d1.getC(30)
d1.setC()
d1.getD(40)
d1.setD()
