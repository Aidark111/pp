class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a 
        self.b = b
        self.c = c 
        
    def is_triangle(self):
        if self.a<=0 or self.b<=0 or self.c<=0:
            print("negative")
        elif self.a + self.b <= self.c or self.a + self.c <= self.b  or  self.b + self.c <= self.a:
            print("Yes we can make triangle")
        else: 
            print("No we cant make tringle")
            
a=int(input("Enter: "))
b=int(input("b "))
c=int(input("c "))

triangle = TriangleChecker(a,b,c)
triangle.is_triangle()
