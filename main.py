import random
def start():
  name = input("Enter your name: ")
  print(f"Welcome {name}")
  user_action = input("Enter a choice (r, p, or s): ")
  possible_actions = ["R", "P", "S"]
  computer_action = random.choice(possible_actions)
  print(f" Player({user_action.upper()}): CPU({computer_action})")
  if user_action.upper() == computer_action:
    print(f"Both players selected {user_action.upper()}. It's a tie!")
    start()
  elif user_action.upper() == "R":
    if computer_action == "S":
      print("Rock smashes scissors! You win!")
    else:
      print("Paper covers rock! CPU wins!.")
  elif user_action.upper() == "P":
    if computer_action == "R":
      print("Paper covers rock! You win!")
    else:
      print("Scissors cuts paper! CPU wins!.")
  elif user_action == "S":
    if computer_action == "P":
      print("Scissors cuts paper! You win!")
    else:
      print("Rock smashes scissors! CPU wins!")
  else :
    print("Incorrect entry . TRY AGAIN.")
    start()

start()