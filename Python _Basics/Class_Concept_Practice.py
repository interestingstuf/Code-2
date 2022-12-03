"""
B = 10
H = 6



print(B * H)
"""






"""
class Area1:
    def __init__(self, B, H, R):
        self.B = B
        self.H = H
        self.R = R
    def calc_Rectangle(self):
        Area = self.B * self.H
        print(Area)
    def calc_cirle(self):
        Area = self.R * self.R * 3.14
        print(Area)
    def peri_rectangle(self): 
        peri = 2 * (self.B+self.H) 
        print(peri)  
A1 = Area1(10, 30, 7)
A1.calc_Rectangle()
B1 = Area1(22, 67, 5)
B1.calc_Rectangle()
C1 = Area1(5, 6, 7)
C1.calc_cirle()
C1.peri_rectangle()
"""
#A App That Shows the Price Of A Certain Phone
class Phone_Price:

    def __init__(self, P, M):
        self.p = P
        self.m = M
    

    def Store_Price(self):
        print("The Price Of", self.m, "is", self.p)
        

    


m = Phone_Price(1000, "Samsung")
m.Store_Price()


