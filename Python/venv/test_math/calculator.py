
class Count:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        anser=self.a+self.b
        return anser
    def sub(self):
        anser=self.a-self.b
        return anser

class Check:
    def __init__(self,num):
        self.num=int(num)

    def is_prime(self):
        if self.num <=1:
            return False
        for i in range (2,self.num):
            if self.num%i ==0:
                return False
        return True