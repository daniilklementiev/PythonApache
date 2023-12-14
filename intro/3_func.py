# Python introduction: functions and scope
x = 10

def get_x():   # function definition
    return x   # x is global

def main():
    print("x = ", get_x())

if __name__ == "__main__": main()