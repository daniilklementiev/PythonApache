# Python introduction: functions and scope
x = 10

def get_x():   # function definition
    return x   # x is global

def hello(name:str="Anonymous") -> str:
    return f"Hello, {name}!"

def change_x(value: int = 20) -> None:
    x = value
    print("Change x to ", x)

def set_x(value):
    global x
    x = value
    print("Set x to ", x)

def pair() :
    return x, 2*x


def main():
    print("x = ", get_x())
    print(hello())
    change_x(1.5)
    print("x = ", get_x())
    set_x(value=30)
    print("x = ", get_x())
    y,w = pair()
    print(f"y={y}, w={w}")

    print("y=%d, w=%d" % pair())

if __name__ == "__main__": main()

