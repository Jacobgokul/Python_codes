import random
print("WELCOME TO THE BOARD")
def players():
    print("Select players")
    global player
    player = int(input())
    game()
    
def game():
    if player == 1:
        player1_name = input("Enter player name: ")
        print("Player 2 will be computer")
        # player 1 to selct the number
        number_1 = int(input(player1_name + " select the number : "))
        number_2 = random.randint(1,10)
        print("computer's number were " +format(str(number_2)))

    #   check its equal
        if number_1 > number_2:
            print(player1_name +" won the match")
        elif number_1 < number_2:
            print(player1_name +" loss the match")
        else:
            print ("DRAW")
    elif player == 2:
        player1_name = input("Enter player name: ")
        player2_name = input("Enter player name: ")
        # player 1 & 2 to selct the number
        number_1 = int(input(player1_name + " select the number : "))
        number_2 = int(input(player2_name +" select the number : "))
        # check its equal
        if number_1 > number_2:
            print(player1_name + " won the match")
        elif number_1 < number_2:
            print(player2_name + " won the match")
        else:
            print("DRAW")
    else:
        print("Only two players are allowed")
        players()
    
    if input("wanna play again(yes/no): ") == "yes":
        game()
    else:
        print("game over")

players()
