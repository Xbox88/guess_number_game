import random
random_num = random.randint(1,100)

count = 0

while True:
    user_guess = int(input("Please guess a number between 1-100: "))
    count +=1

    if user_guess >random_num:
        print("Too big!")

    elif user_guess <random_num:
        print("Too Small!")

    else:
        print(f"Congratulation!,the random number is {random_num}")
        break
print(f"You Have guessed {count} times.")









