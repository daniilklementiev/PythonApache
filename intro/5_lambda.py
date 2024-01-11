# Python lambda functions

lam1 = None
lam2 = None
y = 30
w = 30
def init_lam1():
    global lam1
    y = 10
    lam1 = lambda x: print(x, y)

def init_lam2():
    global lam2
    lam2 = lambda x: print(x, w)



def main() -> None:
    global w
    y = 20
    init_lam1()
    init_lam2()
    w = 20
    lam1("Hello")
    lam2("Hello")

    lam3 = lambda x,y: print(x,y)
    lam3(10,"asd")
    lam4 = lambda : print("no args")
    lam4()
    # IIFE
    (lambda : print( "IIFE" ))()
    # strategy: lambda function as argument

    

if __name__ == "__main__": main()