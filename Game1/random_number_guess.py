import random 

print("\n\nWelcome to number Guessing Game!\n\n")

num = random.randint(1,100)
print(num)
count =0

while True:
    count+=1
    guess = int(input("Enter Your Guessing Number:"))
    if guess>num:
        print("Little Lower")
    elif guess<num:
        print("Little Greter")
    else :
        print("\n\nYou guessed it Correct :",guess," in ",count," Guesses\n\n")
        break


