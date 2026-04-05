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
class C(B):
    def getC(self,c):
        self.c=c
    def setC(self):
        print("C :",self.c)
c1=C()
c1.getA(10)
c1.setA()
c1.getB(20)
c1.setB()
c1.getC(30)
c1.setC()
