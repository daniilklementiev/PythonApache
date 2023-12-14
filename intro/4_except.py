# Python exceptions

def throw() -> None:
    print("Raising error")
    raise TypeError

def throw_msg() -> None:
    print("Raising error")
    raise ValueError("Value error")

def no_throw() -> None:
    pass


def main() -> None:
    try:
        throw()
    except TypeError:
        print("Caught error")
    
    try:
        throw_msg()
    except ValueError as e:
        print("Caught error: ", e.args[0])
    except TypeError:
        print("Caught error type error")
    except :
        print("Unknown error")
    finally:
        print("Finally block")

    try:
        no_throw()
    except :
        print("Caught error")
    else:
        print("No error")
    finally:
        print("Finally block")


        
if __name__ == "__main__": main()