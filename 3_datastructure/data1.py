
l1=[11,12,33,44,55]
print(l1)

l2=['tsla','goog','amzn',44,55,7.7]
print(l2)

#indexing
print(l2[-1])

#slicing
print(l2[0:2])
print(l2)
#append
l2.append('nifty')

#insert
l2.insert(1,700)
print(l2)

s1='jpmorgan'
s1=s1.replace('j','s')
print(s1)

#remove
l2.remove(7.7)
print(l2)

#pop
l2.pop(0)
print(l2)

#del
del l2[1]
print(l2)

print(l1+l2)
l1.extend(l2)
print(l1)

#tuple
p1=(22,33,44,55)
print(p1)
print(p1.index(22))

#indexing and slicing
print(p1[0])
print(p1[0:3])