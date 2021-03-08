

import random
number=random.randint(1,10)
player_name=input("hello!whats your name")
number_of_guesses=0
print('okay!' +player_name+ ' i am guessing a number between 1 and 10')

while number_of_guesses<5:
    guess=int(input())
    number_of_guesses+=1
    if guess<number:
        print("guessed number is too low")
    if guess>number:
        print("guessed number is too high")
    if guess==number:
        break
if guess==number:
    print("your guess is correct" +str(number_of_guesses)+  'tries')
else:
    print("your guess is wrong,the number was" +str(number))



