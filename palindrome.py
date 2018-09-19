print("Welcome to Kev's Palindrome program")

def isPalindrome(arr):
    for i in range(0, len(arr) - 1):
        end = len(arr) - 1 - i
        if i == end:
            return True
        elif arr[i] != arr[end]:
            return False    

cont = True

while cont == True:
    
    word = input("Enter word to check if it's a palindrome: ")
    
    wordArr = []
    
    for i in range(0, len(word)):
        wordArr.append(word[i])

    result = isPalindrome(wordArr)

    if result == True:
        print("Your word is a palindrome!")
    else:
        print ("Your word is not a palindrome!")

    choice = input("Do you want to continue? y/n: ").lower()
    if choice == "n":
        print("Goodbye!")
        cont = False
        break
    elif choice != "y":
        "Invalid input, Goodbye!"