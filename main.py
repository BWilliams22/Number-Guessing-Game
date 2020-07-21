import random

gameover = False 

while not gameover: 
  computer = random.randint(0 ,10)
  player = -1
  tries = 0
  while player != computer: 
    player=int(input("Guess a number from 0-10:"))
    tries += 1
    if player == computer:
      print ("Congratuations you did it!")
      print (f"You guessed it in {tries} tries.") 
    elif player > computer:
      print ("Sorry, you are too high! Guess again!")
    elif player < computer: 
      print ("Sorry, you are too low...try again!")
  choice = input("Play again? (y or n?)")
  if choice != "y":
    gameover = True 

 

