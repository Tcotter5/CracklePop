#if the number is divisible by 3, print Crackle instead of the number
#if number is divisible by 5, print Pop.
#if number is divisible by both 3 and 5, print CracklePop.

for num in range(1, 101):
        if num % 15 == 0:
                print ("CracklePop")
        elif num % 5 == 0:
                print("Pop")
        elif num % 3 == 0:
                print("Crackle")
        else: print(num)
        