import random as rnd
min_dec = 1
max_dec = 64
while True:
    x = rnd.randint(min_dec,max_dec)
    print("Decimal: " + str(x))
    y = input("YOUR ANSWER: ")
    x = bin(x)[2:]
    x = int(x)
    y = int(y)
    print("your answer: " + str(y))
    print("Answer: "+ str(x))
    

    
    
    if(str(y) == str(x)):
        print("Correct")
    else:
        print("Incorrect")
    print("\n\n")
