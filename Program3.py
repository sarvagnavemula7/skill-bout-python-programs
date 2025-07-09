#Create a function called divide(a, b) that returns the result of a / b.
#Use try...except to handle divide-by-zero errors and display a user-friendly message.

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Divide by zero"

a=int(input("Enter Numerator :"))
b=int(input("Enter Denominator :"))

ans=divide(a,b)
print(ans)