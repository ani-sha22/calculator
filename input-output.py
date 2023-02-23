from addition import addition
from multiplication import multiply
from subtract import sub

print("Hello User!\nWelcome to simple calculator\n")
num1 = int(input("Enter number 1 : "))
op = input("Enter operation as symbol : ")
num2 = int(input("Enter number 2 : "))
print("yolo")
print("hello kya haal chaal soniye")

if(op == '+'): print("Output = ",addition(num1,num2));
if(op == '-'): print("Output = ",sub(num1,num2));
if(op == '*'): print("Output = ",multiply(num1,num2));
