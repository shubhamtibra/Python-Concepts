def decorator1(wrapper2):
    print("decorator1 executing")
    def wrapper1(*args, **kargs):
        print("wrapper1 executing")
        #print(args, kargs)
        result = wrapper2(*args, **kargs)
        return result
    return wrapper1

def decorator2(func):
    print("decorator2 executing")
    def wrapper2(*args, **kargs):
        print("wrapper2 executing")
        result = func(*args, **kargs)
        return result
    return wrapper2


# def main(a, b, op='+'):
#     if (op == '+'):
#         return a+b
#     elif (op == '-'):
#         return a-b
#     return None
# main = decorator(main)

# print (main(1, 2, '-'))
@decorator1
@decorator2 # wrapper2
def func(a, b, c=3):
    print(a, b, c)

func = decorator2(func)
func = decorator1(func)
 
func(2, 4)