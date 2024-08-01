import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images_list = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for scissors."))
if user >2:
    print("Wrong choice.")
else:
    print("Your choice:")
    print(images_list[user])
    computer = random.randint(0,2)
    print("Computer's choice:")
    print(images_list[computer])
    if computer == user:
        print("Draw!")
    elif computer==0 and user==2:
        print("you loose!")
    elif user==0 and computer==2:
        print("You win!")
    elif computer>user:
        print("You loose!")
    else:
        print("you win!")