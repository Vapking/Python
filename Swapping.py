# 1st Technique
a = 6
b = 5

tmp = a
a = b
b = tmp

print("A = ",a)
print("B = ",b)

# 2nd Technique
x = 2
y = 3

x = x+y
y = x-y
x = x-y

print("X = ",x)
print("Y = ",y)

#3rd Technique
p = 7
q = 8

p = p^q
q = p^q
p = p^q

print("P = ",p)
print("Q = ",q)

#4th Technique for python only
m = 10 
n = 12

m,n = n,m

print("M = ",m)
print("N = ",n)