import requests
from threading import Thread
import time, os, sys

def type(string:str):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.025)
  print()
quit=False
def alive(username):
  while not quit:
    r=requests.post("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/check/", json = {"username":username, "checking":False}).json()
    if r["Kick"] == True:
      type("The other player left!")
      type("Re-run the program to play again :D")
      sys.exit()
    time.sleep(4)
print('''
For future referance when playing:
7|8|9 
-+-+-
4|5|6
-+-+-
1|2|3''')
username = input("What's your username: \n")
while not requests.post("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/check/", json = {"username":username,"checking":True}).json()["Username"]:
  print("Pick a different one!")
  username = input("What's your username: \n")

Thread(target = alive, args = (username,)).start()
type("Please wait while we match you up with someone!\nFor a quicker match up, call a partner to play on a different computer!")  
r = requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/"+username).json()
match_id = str(r["match_id"])
x=False
if r["match_found"] == False:
  x=True
  while requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/match/"+match_id).json()["match_found"] == False:
    time.sleep(3)
type("Match FOUND!")


theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
if x==True:
  while True:
    os.system("clear")
    b=requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()["Username"]
    b.remove(username)
    print(f"{username} vs. {b[0]}")
    printBoard(theBoard)
    try:
      if count==0:
        type("Game Over!")
      if r["Win"] == "X":
        type("YOU WON!!!!!!!!!!!!")
        break
      elif r["Win"] == "O":
        type("You lost :(, better luck next time!")
        sys.exit()
    except NameError or KeyError:pass
    type("Your turn!")
    choice = input("Where do you want to place the x? (NumKey Pad order): ")
    if choice not in requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()["Empty"]:
      continue
    r=requests.post("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"X":True, "input":choice, "match_id":match_id}).json()
    count = len(r["Empty"])
    for item in r["X"]:
      theBoard[item] = "x"
    os.system("clear")
    printBoard(theBoard)
    if count==0:
      type("Game Over!")
    if r["Win"] == "X":
      type("YOU won!!!!!!!!!!!!")
      break
    elif r["Win"] == "O":
      type("You lost :(, better luck next time!")
      sys.exit()
    type("Waiting for opponent to make move...")
    try:
      while count == len(requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()["Empty"]):
        time.sleep(2)
    except KeyError:
      if requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()["kicked"]:
        break
    r1=requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()
    for item in r1["O"]:
      theBoard[item] = "o"
else:
  while True:
    os.system("clear")
    b=requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()["Username"]
    b.remove(username)
    print(f"{username} vs. {b[0]}")
    printBoard(theBoard)
    type("Waiting for opponent to make move...")
    r1=requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()
    count = len(r1["Empty"])
    try:
      while count == len(requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()["Empty"]):
        time.sleep(2)
    except KeyError:
      if requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()["kicked"]:
        break
    r2=requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()
    for item in r2["X"]:
      theBoard[item] = "x"
    os.system("clear")
    printBoard(theBoard)
    r=requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()
    try:
      if count==0:
        type("Game Over!")
      if r["Win"] == "O":
        type("you won!!!!!!!!!!!!")
        break
      elif r["Win"] == "X":
        type("You lost :(, better luck next time!")
        sys.exit()
    except KeyError:pass
    
    type("Your turn!")
    while True:
      choice = input("Where do you want to place the o? (NumKey Pad order): ")
      if choice not in requests.get("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"match_id":match_id}).json()["Empty"]:
        print("Sorry thats taken!")
        continue
      else:
        break
    r=requests.post("https://Online-Tic-Tac-Toe-Server.chaoticchaosthegreat.repl.co/server/", json={"X":False, "input":choice, "match_id":match_id}).json()
    for item in r["O"]:
      theBoard[item] = "o"
    os.system("clear")
    printBoard(theBoard)
    if count==0:
      type("Game Over!")
    if r["Win"] == "O":
      type("you WON!!!!!!!!!!!!")
      break
    elif r["Win"] == "X":
      type("You lost :(, better luck next time!")
      sys.exit()
  




