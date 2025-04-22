class swapnumber():
    def swapping(self,a,b):
        a,b=b,a
        return a,b
swap=swapnumber()
print(swap.swapping(2,5))