import time

def fibonacci_sequence(n):
    
    """

    """
    starttime = time.time()

    sigma = 1.61815754

    if n >= 15 & n <= 35:
        value = int(((sigma**n) - (1-sigma)**n)/(5**(1/2)))
    else:
        value = None
        raise ValueError("Error: Method takes an n value from 15 to 35")
    
    endtime = time.time()

    if value != None:
        print(f"fib({n}) = {value}")
        print(f"fib({n}) took {endtime - starttime} seconds")

if __name__ == "__main__":
    fibonacci_sequence(34)
