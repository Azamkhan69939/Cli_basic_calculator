from arithm import *
def cal():
    print(" "*50,"CLI CALCULATOR")
    print("*"*100)
    print(" "*55,"WELCOME")
    print("-"*100)
    print(" "*55,"Main menu")
    run=True
    while(run):
        print("-"*100)
        print(main_menu,end="")
        try:
            op=int(input("enter a choice:"))
        except ValueError:
            print("please enter a valid number")
        match op:
            case 1:
                normal_operations()
            case 2:
                more_operations()
            case 3:
                swap_operations()
            case 4:
                print('See ya!')
                run=False
cal()
 