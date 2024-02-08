#Code for a simple calculator program

a = float(input("Enter First Number:"))
op =  input("Enter Operator:")
b = float(input("Enter Second Number:"))

if op == '/':
    print(a/b)
else:
    print("Error")

# if  op=='+':
# print(a+b)

# elif op=="-":
# print(a-b)

# #print("The result of ",a,op,b," is :",a+b)
# else:
# print("Invalid operator")