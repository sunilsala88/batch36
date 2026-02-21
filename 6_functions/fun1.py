
#function defination:
#function is a block of code which performs a specific task and can be reused whenever required.

#function call:
#function call is the process of executing a function by its name and passing the required arguments.


def find_highest(list1):

    high=list1[0]
    for i in list1:
        if high<i:
            high=i
    return high


list1=[5, 12, 3, 21, 7]
high=find_highest(list1)
print(high)

m=max(list1)
print(m)