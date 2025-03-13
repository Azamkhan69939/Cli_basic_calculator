import math
def conversion(deg):
    return deg*(math.pi/180)

def input_nums():
    try:
        number1=int(input("enter a first number:"))
        number2=int(input("enter a second number:"))
    except ValueError:
        print("please enter a valid number")
    return number1,number2

def input_num():
    try:
        number1=int(input("enter a first number:"))
    except ValueError:
        print("please enter a valid number")
    return number1

def nor_operation(number1,number2,op):
    print(eval(f'{number1}{op}{number2}'))

def square_operation(number1,op):
    print(eval(f'{number1}{op}{2}'))

def cube_operation(number1,op):
    print(eval(f'{number1}{op}{3}'))

def mod(number1):
    if number1>0:
        print(number1)
    else:
        print(-number1)
def  sqrt(number1):
    print(math.sqrt(number1))

def sin(angle):
    print(f'sin{angle}:{math.sin(conversion(angle))}')

def cos(angle):
    print(f'cos{angle}:{math.cos(conversion(angle))}')

def tan(angle):
    print(f'tan{angle}:{math.tan(conversion(angle))}')

def swap(number1,number2,op):
    number1,number2=number2,number1
    print("number swaped")
    nor_operation(number1,number2,op)