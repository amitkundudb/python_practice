#Sequence of Elements returns new sequence of elements
l = [1,2,3,4,5,6]
cube = lambda x:x*x*x
newl = list(map(cube,l))
print(newl)