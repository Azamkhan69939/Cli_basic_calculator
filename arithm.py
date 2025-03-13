from const import *
from operations import *
def normal_operations():
    run=True
    while(run):
        print("*"*100)
        print(" "*50,"Normal Mode")
        print(Normal_options)
        try:
            oper=int(input("enter a choice:"))
        except ValueError:
            print("please enter a valid number")
        match oper:
            case 1:
                number1,number2=input_nums()
                nor_operation(number1,number2,add_op)
            case 2:
                number1,number2=input_nums()
                nor_operation(number1,number2,sub_op)
            case 3:
                number1,number2=input_nums()
                nor_operation(number1,number2,mul_op)
            case 4:
                number1,number2=input_nums()
                nor_operation(number1,number2,div_op)
            case 5:
                run=False

def more_operations():
    run=True
    while(run):
        print("*-"*50)
        print(" "*50,"More Mode")
        print(more_options)
        try:
            oper=int(input("enter a choice:"))
        except ValueError:
            print("please enter a valid number")
        match oper:
            case 1:
                number1,number2=input_nums()
                nor_operation(number1,number2,pow_op)
            case 2:
                number1=input_num()
                square_operation(number1,pow_op)
            case 3:
                number1,number2=input_num()
                cube_operation(number1,pow_op)
            case 4:
                number1=input_num()
                mod(number1)
            case 5:
                number1=input_num()
                sqrt(number1)
            case 6:
                number1=input_num()
                sin(number1)
                cos(number1)
                tan(number1)
            case 7:
                run=False
def swap_operations():
    run=True
    while(run):
        print("-*"*50)
        print(" "*50,"Swap Mode")

        print(swap_options)
        try:
            oper=int(input("enter a choice:"))
        except ValueError:
            print("please enter a valid number")
        match oper:
            case 1:
                number1,number2=input_nums()
                swap(number1,number2,sub_op)
            case 2:
                number1,number2=input_nums()
                swap(number1,number2,div_op)
            case 3:
                run=False