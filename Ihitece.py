class P:
    def f(self):
        return 10    
class c(P):
    def f(self):
        return super().f()-5
o=c()
print(o.f())        