def FibonnaciSequence(number):
    if number <= 1:
        return number
    else:
        return(FibonnaciSequence(number-1) + FibonnaciSequence(number-2))


figure = int(input("Enter a figure to give you a sequence?"))

if figure <= 0:
    print("Please enter a positive number")
else:
    print("The fibonacci series up to " + str(figure) + " is: ")
    for i in range(figure):
        print(FibonnaciSequence(i))
