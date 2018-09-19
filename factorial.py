
def factorial(num):
    factor = 1
    for i in range(num - 1, 0, -1):
        factor = factor + factor*i
        
    return factor

print ("Welcome to Kev's Facorial calculator!")

cont = True

while cont == True:
    number = int(input("Enter number: "))
    answer = factorial(number)
    print("{0} factorial is: {1}".format(number, answer))

    choice = input("Do you want to continue? y/n: ").lower()
    if choice == "n":
        print("Goodbye!")
        cont = False
        break
    elif choice != "y":
        print("Invalid input, Goodbye!")
        cont = False


