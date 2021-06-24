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

asset_list = [rock,paper,scissors]
user_choose = int(input("What do you choose? Type\n 0 : Rock\n 1 : Paper\n 2 : Sccissors\n Ans : "))
computer_choose = random.randint(0,2)

if(user_choose==0) and (computer_choose==0):
    print("You Choose: " + asset_list[user_choose])
    print("Computer Choose: " + asset_list[computer_choose])
    print("*******************************")
    print("         GAME DRAW")
    print("*******************************")
elif (user_choose==0) and (computer_choose==1):
    print("You Choose: " + asset_list[user_choose])
    print("Computer Choose: " + asset_list[computer_choose])
    print("*******************************")
    print("         COMPUTER WIN")
    print("*******************************")
elif (user_choose==0) and (computer_choose==2):
    print("You Choose: " + asset_list[user_choose])
    print("Computer Choose: " + asset_list[computer_choose])
    print("*******************************")
    print("         YOU WIN")
    print("*******************************")
elif (user_choose==1) and (computer_choose==0):
    print("You Choose: " + asset_list[user_choose])
    print("Computer Choose: " + asset_list[computer_choose])
    print("*******************************")
    print("         YOU WIN")
    print("*******************************")
elif (user_choose==1) and (computer_choose==1):
    print("You Choose: " + asset_list[user_choose])
    print("Computer Choose: " + asset_list[computer_choose])
    print("*******************************")
    print("         GAME DRAW")
    print("*******************************")
elif (user_choose==1) and (computer_choose==2):
    print("You Choose: " + asset_list[user_choose])
    print("Computer Choose: " + asset_list[computer_choose])
    print("*******************************")
    print("         COMPUTER WIN")
    print("*******************************")
elif (user_choose==2) and (computer_choose==0):
    print("You Choose: " + asset_list[user_choose])
    print("Computer Choose: " + asset_list[computer_choose])
    print("*******************************")
    print("         COMPUTER WIN")
    print("*******************************")
elif (user_choose==2) and (computer_choose==1):
    print("You Choose: " + asset_list[user_choose])
    print("Computer Choose: " + asset_list[computer_choose])
    print("*******************************")
    print("         YOU WIN")
    print("*******************************")
elif (user_choose==2) and (computer_choose==2):
    print("You Choose: " + asset_list[user_choose])
    print("Computer Choose: " + asset_list[computer_choose])
    print("*******************************")
    print("         GAME DRAW")
    print("*******************************")
else:
    print("PLEASE SELECT CORRECTLY")
