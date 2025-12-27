

# Rest parameters in functions: A function can accept a variable number of arguments using *args, which collects them into a tuple
def my_function(*args):
    for index, value in enumerate(args):
        print(f"Argument {index}: {value}") 
my_function(10, 20, 30, "Hello", True)