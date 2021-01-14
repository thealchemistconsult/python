#  modifying functions and passing the output in other functions

def announce(f):
    def wrapper():
        print("About to run a function")
        f()
        print("Done with the function")
    return wrapper


@announce
def Hello():
    print("hello World")


Hello()
