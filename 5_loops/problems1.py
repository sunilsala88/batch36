

list1=[5, 12, 3, 21, 7]
high=list1[0]
for i in list1:
    if high<i:
        high=i

print(high)

i=0
high=list1[0]
while True:
    if i>=len(list1):
        break
    if high<list1[i]:
        high=list1[i]
    i=i+1

print(high)