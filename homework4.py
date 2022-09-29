import random

stick = int(input("How many sticks (N) in the pile : "))      # input the number of stick to the game

while stick < 0 :                                             # check the number of stick [should be more than 1 stick]
  print("Please input more than 1 pile to start the game.")
  stick = int(input("How many sticks (N) in the pile : "))

name = input("What is you name? : ")                          # input player name
take = stick
count = 0

while stick >= 0 :                                            # check the number of stick [condition more than 1]
  if (count%2 != 0):                                          # let computer start first!
    print(name , end="")
    take = int(input(", how many sticks you will take (1 or 2)? : "))   # player turn
    if (3 > take > 0) and (stick >= take) :                   # set that player can take only 1 or 2 sticks
      ans = stick - take                      # to check last stick
      stick = stick - take                    # assign new value to stick
      #print(stick)
      count += 1
      #print(count)
      if ans == 0 :                           # player takes last stick, computer win! and break to finish
        print(name , end="")
        print(", takes the last stick.")
        print("I, smart computer, win!!!")
        #print(stick)
        break
      else :
        print("There are ", ans, "sticks in the pile.")
        #print(stick)
    elif take >= 3 :                                          # the condition : player takes more than 2 sticks
      print("No, you cannot take more than 2 sticks!")
      #print(stick)       
    elif take > stick :                                       # the condition : player takes more than sticks in pipe
      print("There are not enough sticks to take.")
      #print(stick)
    elif take <= 0 :                                          # the condition : player takes less than 0
      print("No, you cannot take less than 1 stick!") 
      #print(stick)
      
  else :                                                      # computer turn  
    if stick%3 == 0 :                                         # the condition that computer will take 2 sticks
      take = 2
      print("I, smart computer, takes : ", take)
      ans = stick - take                                      # to check last stick
      stick = stick - take                                    # assign new value to stick
      count += 1
      print("There are ", ans, "sticks in the pile.")
      #print(stick)
    elif stick%3 == 2 :                                   # the condition that computer will take only 1 stick
      take = 1
      print("I, smart computer, takes : ", take)
      ans = stick - take                                    # to check last stick    
      stick = stick - take                                  # assign new value to stick
      #print(stick)
      count += 1
      if ans == 0 :                                         # computer takes last stick, player win! and break to finish
        print("I, smart computer, takes the last stick.")       
        print(name , end="")
        print(" wins (I, smart computer, am sad T_T)")
        #print(stick)
        break 
      else :
        print("There are ", ans, "sticks in the pile.")
        #print(stick)
    else :                                                  # other conditions, computer takes random stick 1 or 2
      take = random.randint(1,2)                            # take = random number 1 or 2
      print("I, smart computer, takes : ", take)
      ans = stick - take                                    # to check last stick    
      stick = stick - take                                  # assign new value to stick
      #print(stick)
      count += 1
      if ans == 0 :                                         # computer takes last stick, player win! and break to finish
        print("I, smart computer, takes the last stick.")       
        print(name , end="")
        print(" wins (I, smart computer, am sad T_T)")
        #print(stick)
        break 
      else :
        print("There are ", ans, "sticks in the pile.")
        #print(stick)