choices = {'R': 'S', 'S': 'P', 'P':'R'}

# Setting count to 0
player1 = 0
player2 = 0
draw = 0

# open the both files in the same time and creating 2 lists for handling the items
with open('player1.txt', 'r') as play1, open('player2.txt', 'r') as play2:
    items1 = [choice1.strip() for choice1 in play1]
    items2 = [choice2.strip() for choice2 in play2]
    # player1_wins, player2_wins, draws = sum(choices[choice1] == choice2 for choice1, choice2 in zip(items1, items2)), sum(choices[choice2] == choice1 for choice1, choice2 in zip(items1, items2)), sum(choice1 == choice2 for choice1, choice2 in zip(items1, items2))

    # iterate over the lists created in the same time using zip and comparing choices in the dictionary choice
    for choice1, choice2 in zip(items1, items2) :
        if choices[choice1] == choice2:
            player1 += 1 
        elif choices[choice2] ==  choice1: 
            player2 += 1
        else:
            draw += 1
            
                
# creating the file results.txt and write into it the counting for each
with open('results.txt', 'w') as result:
    result.write(f"Player1 wins: {player1}" + '\n')
    result.write(f"Player2 wins: {player2}" + '\n')
    result.write(f"Draws: {draw}"+ '\n')
    
