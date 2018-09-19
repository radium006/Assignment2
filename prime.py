print("Welcome to Kev's Prime Number Application")

cont = True

def primeNumber(num):
    
    for x in range(2,num-1):
        if num % x == 0:
            return False
    return True


while cont == True:
    
    number = int(input("Enter number to check if it's prime: "))
    isPrime = primeNumber(number)
    
    if isPrime == True:
        print("{0} is prime!".format(number))
    else:
        print("{0} is NOT prime!".format(number))

    choice = input("Do you want to continue? y/n: ").lower()
    if choice == "n":
        print("Goodbye!")
        cont = False
        break
    elif choice != "y":
        print("Invalid input, Goodbye!")
        cont = False
    