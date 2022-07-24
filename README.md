# DS270702-SticksInThePipe
## _The Pipe Game is the game that allows you to play with Python._
The Rule : The player that takes the last stick will lose.
- You play as the Player1
- Python plays as the Player2

## _Game Start!_
 To start the game, you have to input more than one stick.
```sh
while stick < 0 :
  print("Please input more than 1 pile to start the game.")
  stick = int(input("How many sticks (N) in the pile : "))
```

## _The result of the program_
 a) In case of you win! : From code, the program will show the result as below.

```sh
if ans == 0 :
  print("I, smart computer, takes the last stick.")
  print(name , end="")
  print("wins (I, smart computer, am sad T_T)")
  break
```
- Example<br />
How many stick (N) in the pipe : 5<br />
What is your name? : Alice<br />
Alice, how many sticks you will take (1 or 2)? : 1<br />
There are 4 sticks in the pipe.<br />
I, smart computer, takes : 2<br />
There are 2 sticks in the pipe.<br />
Alice, how many sticks you will take (1 or 2)? : 1<br />
There are 1 sticks in the pipe.<br />
I, smart computer, takes : 1<br />
I, smart computer, takes the last stick.<br />
Alice wins (I, smart computer, am sad T_T)<br />



b) In case of Python wins! : From code, the program will show the result as below.

```sh
if ans == 0 :
  print(name , end="")
  print(", takes the last stick.")
  print("I, smart computer, win!!!")
  break
```
- Example<br />
How many stick (N) in the pipe : 5<br />
What is your name? : Alice<br />
Alice, how many sticks you will take (1 or 2)? : 1<br />
There are 4 sticks in the pipe.<br />
I, smart computer, takes : 2<br />
There are 2 sticks in the pipe.<br />
Alice, how many sticks you will take (1 or 2)? : 2<br />
Alice, takes the last stick.<br />
I, smart computer, win!!!<br />

c) In case of ERROR : 
- Player takes more than 2 sticks.
```sh
elif take >= 3 :
  print("No, you cannot take more than 2 sticks!")
```
Alice, how many sticks you will take (1 or 2)? : 4<br />
No, you cannot take more than 2 sticks!<br />

- Player takes sticks more than sticks which remain in the pipe.
```sh
elif take > stick :
  print("There are not enough sticks to take.")
```
There are 1 sticks in the pipe.<br />
Alice, how many sticks you will take (1 or 2)? : 2<br />
There are not enough sticks to take.<br />

- Player takes less than 1 stick.
```sh
elif take <= 0 :
  print("No, you cannot take less than 1 stick!")
```
Alice, how many sticks you will take (1 or 2)? : -1<br />
No, you cannot take less than 1 stick!<br />

