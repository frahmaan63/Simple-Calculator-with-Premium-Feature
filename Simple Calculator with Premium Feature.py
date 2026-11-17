# Simple Calculator with Premium Feature
# FR's Python Project

import math
REDEEM_CODE = {"ARCHIMEDES63", "PHYTAGORAS92"}  # List of Valid Reedem Code

def basic_calculator():
    number1 = int(input("First Number : "))
    operator = input("Operator (+, -, *, /, %, //): ")
    number2 = int(input("Second Number: "))
    if operator == "+": print("Result :", number1 + number2)
    elif operator == "-": print("Result :", number1 - number2)
    elif operator == "*": print("Result :", number1 * number2)
    elif operator == "/": print("Result :", number1 / number2 if number2 != 0 else "Cannot be divided by 0")
    elif operator == "%": print("Result :", number1 % number2)
    elif operator == "//": print("Result :", number1 // number2 if number2 != 0 else "Cannot be divided by 0")
    else: print("Unknown Operator")

def premium_calculator():
    print("1. Square Root  2. Exponentiation  3. Logarithm  4. Sine 5. Cosine 6. Tangent 7. Fibonacci 8. Factorial")
    select = input("Select Feature : ")
    if select == "1":
        print("Result:", math.sqrt(float(input("Number : "))))
    elif select == "2":
        a = float(input("Base : ")); b = float(input("Exponent : "))
        print("Result :", a ** b)
    elif select == "3":
        print("Result :", math.log10(float(input("Number : "))))
    elif select == "4":
        print("Result :", math.sin(math.radians(float(input("Angle (degrees): ")))))
    elif select == "5":
        print("Result :", math.cos(math.radians(float(input("Angle (degrees): ")))))
    elif select == "6":
        print("Result :", math.tan(math.radians(float(input("Angle (degrees): ")))))
    elif select == "7":
        n = int(input("Enter the number of Fibonacci numbers:"))
        a, b = 0,1
        print("Fibonacci Sequence :")
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
    elif select == "8":
        def factorial(n):
            if n == 1:
                return(n)
            else:
                return(n*factorial(n-1))
        n = int(input("Input Numbers :"))
        print("%d! = %d" % (n, factorial(n)))

def main():
    premium = False
    while True:
        print("\n=== CALCULATOR ===")
        print("1. Basic Calculator")
        print("2. Premium Calculator")
        print("3. Redeem Premium Code")
        print("0. Exit")
        menu = input("Select: ")

        if menu == "1":
            basic_calculator()
        elif menu == "2":
            if premium:
                premium_calculator()
            else:
                print("This Feature Is Exclusive Only for Premiums, Please Redeem Premium Code By Selecting Menu 3.")
        elif menu == "3":
            code = input("Premium Code : ").strip()
            if code in REDEEM_CODE:
                premium = True
                print("Premium Feature Available")
            else:
                print("Invalid Code")
        elif menu == "0":
            break

main()
