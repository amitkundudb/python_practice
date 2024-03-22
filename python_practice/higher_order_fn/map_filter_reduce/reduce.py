from functools import reduce
num = [1,2,3,4,5]
def mysum(x,y):
    return x+y
sum1 = reduce(mysum,num)
print(sum1)