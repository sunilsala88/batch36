
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
    num1=int(input('enter a number'))
    num2=int(input('enter a number(zero is not allowed)'))
    ans=num1/num2
    print(ans)
except ZeroDivisionError :
    print('zeor is not allowed')
except ValueError:
    print('dont type alphabet as input')
