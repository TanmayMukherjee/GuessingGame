import random



# generate random integer values
number = random.randint(0, 10)
chances=0
print("Guess A Number(between 1 and 10): ")

while chances < 5:
    guess=int(input("Enter Your Guess: "))
    if guess==number:
        print("Congrats!You have Won!!")
        break
    elif(guess < number):
        print("Your Guess Was Too Low:Guess A Number Higher Than ",guess)
    else:
        print("Your Guess Was Too High:Guess A Lower Number Than ",guess)


     
