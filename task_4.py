import random
choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, scissors: ")

computer_choices = random.choice(choices)

print(f"\nyou chose: {user_choice}")
print(f"computer chose: {computer_choices}")

if user_choice == computer_choices:
    print("its a tie!")

elif(
    (user_choice == 'rock' and computer_choices == 'scissors')or
    (user_choice == 'paper' and computer_choices == 'rock')or
    (user_choice == 'scissors' and computer_choices == 'paper')):

    print("you win!")

else:
     print("computer wins!")