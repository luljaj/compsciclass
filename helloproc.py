# define the squaring function
def sqr(x):
    y = x*x
    return y

# define the procedure

def greet(n):
    print(f'Hello, {n}')

#call/exc the procedure
name= input('Enter name: ')
greet(name)

num = int(input("Enter number: "))
num2 = sqr(num)

print(f'Hello, {name}. If you like {num} then you\'ll love {num2}')