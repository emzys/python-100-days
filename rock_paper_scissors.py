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

moves = [rock, paper, scissors]
player_move = int(
    input(
        "What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n"
    ))

if player_move > 2:
    print("You typed an ivalid number!")
else:
  computer_move = random.randint(0, 2)
  
  print(f"\nYour move ({player_move}): \n{moves[player_move]}\n")
  print(f"Computer move ({computer_move}): \n{moves[computer_move]}\n")
  
  if player_move == computer_move:
      print("It's a draw!")
  elif player_move == 0 and computer_move == 2:
      print("You win!")
  elif player_move > computer_move:
      print("You win!")
  else:
      print("You lose!")
