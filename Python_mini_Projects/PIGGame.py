import random  

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
while True:
    players = input("Enter The number of player(2-4):")
    if players.isdigit():  #to check input is a valid number
        players = int(players) #converts string to int
        if 2 <= players <= 4:
            break
        else:
            print("No of players must be between 2 to 4")
    else:   
        print("Invalid Entry, Try again!")

print("No of players playing =",players)
    
max_score = 50
player_scores =  [0 for _ in range(players)] #List for storing the scores

while max(player_scores) < max_score:

    for Player_id in range(players):
        print("\nPlayer ID no -",Player_id + 1, "turn has started:)")
        print("Your Score is:", player_scores[Player_id],"\n")
        current_score = 0
        while(True):
            Should_roll = input("Would you like to roll (y)??")
            if Should_roll.lower() != "y":              
                break
            
            value = roll()
            if value == 1:
                print("You rolled 1 !! YOUR TURN IS OVERRR!")
                current_score = 0
                break
            else:   
                current_score += value
                print("You rolled a:", value)
        
            print("Your Score is:", current_score)

    player_scores[Player_id] += current_score
    print("your total score is:", player_scores[Player_id])

Maximum_score = max(player_scores)
winning_id = player_scores.index(Maximum_score)
print("Player ID numer", winning_id + 1, "is the Winner!! with a score of :", max_score,"\n CONGRATULATIONS!!!:)")
    