stick = int(input("How many sticks (N) in the pile : "))

while stick < 0 :
  print("Please input more than 1 pile to start the game.")
  stick = int(input("How many sticks (N) in the pile : "))

name = input("What is you name? : ")
count = 0

while stick >= 0 :
  if (count%2 == 0):
    print(name , end="")
    take = int(input(", how many sticks you will take (1 or 2)? : "))
    if (3 > take > 0) and (stick >= take) :
      ans = stick - take
      stick = stick - take
      #print(stick)
      count += 1
      #print(count)
      if ans == 0 :
        print(name , end="")
        print(", takes the last stick.")
        print("I, smart computer, win!!!")
        #print(stick)
        break
      else :
        print("There are ", ans, "sticks in the pile.")
        #print(stick)
    elif take >= 3 :
      print("No, you cannot take more than 2 sticks!")
      #print(stick)       
    elif take > stick :
      print("There are not enough sticks to take.")
      #print(stick)
    elif take <= 0 :
      print("No, you cannot take less than 1 stick!") 
      #print(stick)
  else :
    import random
    take = random.randint(1,2)
    print("I, smart computer, takes : ", take)
    if (3 > take > 0) and (stick >= take) :
      ans = stick - take
      stick = stick - take
      #print(stick)
      count += 1
      if ans == 0 :
        print("I, smart computer, takes the last stick.")
        print(name , end="")
        print("wins (I, smart computer, am sad T_T)")
        #print(stick)
        break
      else :
        print("There are ", ans, "sticks in the pile.")
        #print(stick)