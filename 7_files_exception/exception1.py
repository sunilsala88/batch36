
# try:
#     num1=int(input('enter a number'))
#     num2=int(input('enter a number(zero is not allowed)'))
#     ans=num1/num2
#     print(ans)
# except Exception as e:
#     print('something went wrong in the code')
#     print(e)

# print('close all position')

#ZeroDivisionError
#ValueError


try:
    with open('/Users/algo trading 2026/batch36/7_files_exception/data.txt', 'r') as f1:
        d=f1.read()
    d=d.split('\n')
    num1=int(d[0])
    num2=int(d[1])
    print(num1,num2)
    ans=num1/num2
    print(ans)
except ZeroDivisionError :
    print('zeor is not allowed')
except ValueError:
    print('dont type alphabet as input')
