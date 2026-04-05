class A:
    def getA(self,a):
        self.a=a
    def setA(self):
        print("A :",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def setB(self):
        print("B :",self.b)
class C(A):
    def getC(self,c):
        self.c=c
    def setC(self):
        print("C :",self.c)
b1=B()
c1=C()
b1.getA(10)
b1.setA()
b1.getB(20)
b1.setB()

c1.getA(40)
c1.setA()
c1.getC(30)
c1.setC()
