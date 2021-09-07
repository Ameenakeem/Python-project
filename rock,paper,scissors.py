wins = 0
lose = 0
draw = 0
while True:
    import random
    computer = random.randint(1,3)

    print("1 = rock 2 = paper 3 = scissor")
    choice = input("Enter a digit between 1-3: ")
    if choice == "1":
        print("you = rock")
    elif choice == "2":
        print("you = paper")
    elif choice == "3":
        print("you = scissor")    
    else:
        print("invalid input")

    if computer == 1:
        print("computer = rock")
    elif computer == 2:
        print("computer = paper")
    elif computer == 3:
        print("computer = scissor")    
    else:
        print("invalid input")


    if choice == "1" and computer == 2:
        print("computer wins")
        lose = lose + 1
    elif choice == "2" and computer == 3:
        print("computer wins")
        lose = lose + 1
    elif choice == "2" and computer == 1:
        print("you wins")
        wins = wins +1
    elif choice == "3" and computer == 2:
        print("you wins")
        wins = wins +1
    elif choice == "3" and computer == 1:
        print("computer wins")
        lose = lose +1
    elif choice == "1" and computer == 3:
        print("you wins")
        wins = wins +1                
    elif choice == "1" and computer == 1:
        print("draw")
        draw = draw + 1
    elif choice == "2" and computer == 2:
        print("draw")
        draw = draw + 1
    elif choice == "3" and computer == 3:
        print("draw")
        draw = draw + 1
    print("a = check your score b = quit c = continue")
    a = "cheak your score"
    b = "quit"
    c = "continue"
    des = input("decide please: ") 
    if des == "a":
        print("you win",wins,"times,you lose",lose,"time,you draw",draw,"times.")
    elif des == "b":
          break
    elif des == "c":
        continue
    else:
        print("I can't understand")
             
