#Day 4 Project - Rock, Scissors, Paper

#==============================================================


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

#Write your code below this line 👇
import random
list = [rock, paper, scissors]
ran = random.randint(0, 2)
choose = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"
    ))
if choose > 2 or choose < 0 :
    result = "lose"
else :
    print(list[choose])
    print("Computer chose:")
    print(list[ran])
    
    num = ran - choose
    if num == 0 :
        result = "draw"
    elif abs(num) == 2 :
        if num < 0 :
            result = "lose"
        else : 
            result = "win"
    elif num > 0 :
        result = "lose"
    else :
        result = "win"
print(f"You {result}")