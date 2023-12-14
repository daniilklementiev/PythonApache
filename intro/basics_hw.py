def input_loop():
    x = 0
    y = 0
    while True:
        x = int(input("Input x = "))
        if x < 0:
            print("x should be positive")
        else:
            break

    while True:
        y = int(input("Input y = "))
        if y < 0:
            print("y should be positive")
        elif y == x:
            print("y should not be equal to x")
        else:
            break
    
    if x > 0 and y > 0 and x != y:
        print("x + y = ", x + y, end=";", sep="", flush=True)

def main():
    input_loop()

if __name__ == "__main__":
    main()