
lucky=7

def average(numbers:list)->int:
    global lucky
    lucky=8
    print(lucky)
    total=0
    for num in numbers:
        total=total+num
    avg=total/len(numbers)
    return avg

l1=[1,2,3,4,5]
a=average(l1)
print(lucky)
print(a)