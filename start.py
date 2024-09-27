num = int(input("enter a number:"))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")    

def palindrome(st):
    if st == st[::-1]:
        print("palindrome")
    else:
        print("not palindrome")    

def square(n):
    print(n**2)
    
def cube(n):
    print(n**3)
    
