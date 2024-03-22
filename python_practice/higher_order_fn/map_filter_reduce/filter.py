def filter_fn(a):
    return a>2
l = [1,2,3,4,6,7]
newnewl = list(filter(filter_fn,l))
print(newnewl)