import math 

def sqrt(x):
    if not isinstance(x, (int,float)):
        raise TypeError("input is not a numerical value")
    if x < 0:
        raise ValueError("input is less than zero")
    return math.sqrt(x)

def sqrt_try(x): 
    try:
        return math.sqrt(x)
    except TypeError:
        print("input is not a numerical value")
    except ValueError:
        print("input is not less than a zero")
    return None

if __name__ == "__main__":
    
    x = 25
    print(sqrt(x))
    
    x = "a"
    #print(sqrt(x))
    print(sqrt_try(x))
    x = -121
    print(sqrt_try(x))
    
    