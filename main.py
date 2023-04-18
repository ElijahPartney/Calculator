import os

def Calculator():
    opperator = input("Enter a Operation Sign (+  -  *  /): ")
    print("\n")
    num1 = float(input("Enter the 1st Number :"))
    num2 = float(input("Enter the 2nd Number :"))
    print("\n")
    if opperator == "+":
        result = num1 + num2
    elif opperator == "-":
        result = num1 - num2
    elif opperator == "*":
        result = num1 * num2
    elif opperator == "/":
        result = num1 / num2
        
    print("The answer is " + str(result))
    
    finisher()
    
def finisher():
    
    print("\n")
    again = input("Have another Question? (Y/N) \n:")
    if again == "N":
        os.system('cls')
        breakpoint
        
    elif again == "Y":
        os.system('cls')
        Calculator()
        
Calculator()
