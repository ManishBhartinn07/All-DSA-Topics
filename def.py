# def name():
#     n = input("Enter your name: ")
#     print(n)

# name()

# x=int(input())
# y=int(input())
# if x > y:
#     print("x is Greater")

# def main():


def main():
    n=int(input())
    if(is_Even(n)):
        print("Even")
    else:
        print("Odd")

def is_Even(n):
    return n%2 == 0 

main()

