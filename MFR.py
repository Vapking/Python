from functools import reduce

Number = [3,2,5,7,4,6,8,9,1]

evens = list(filter(lambda n : n%2==0,Number))

print(evens)

double = list(map(lambda n : n-2,evens))

print(double)

sum = reduce(lambda a,b : a+b,double)

print(sum)