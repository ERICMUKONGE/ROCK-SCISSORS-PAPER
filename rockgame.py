import random

player = input("Enter a choice\nRock\nScissor\nPaper:\n")

possible_action = ["Rock","Scissor","Paper"]
computer_player = random.choice(possible_action)

if player == computer_player:
    print("Both player Select >" + player +"< it's tie")

elif player == "rock":
    if computer_player == "scissor":
        print("Rock smashes scissor! you win")
    else:
        print("Paper cover Rock! you lose")

elif player == "paper":
    if computer_player == "rock":
        print("Rock smashes scissor! you win")
    else:
        print("Scissor cuts paper! you lose")

elif player == "scissors":
    if computer_player == "paper":
        print("Scissor covers rock! you win!")

    else:
        print("Rock smashes scissor ! you lose")                    