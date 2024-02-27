import random



def roll():
     min_number = 1 
     max_number = 7
     random_number = random.randint(min_number,max_number)
     return random_number

while True:
     players = int(input("how many players want to play ? (max 4 players) : "))
     if 1 < players <= 4 :
          print(f"you selecet {players} players")
          break
     else:
          print(" invalid players number , try again ")
          

max_score = 51
players_score = [0 for _ in range(players)]


while max(players_score) < max_score  :
     for players_index in range(players) :
          current_score = 0
          
          while True : 
               roll_chance = input(f"do you wanna roll player {players_index + 1} ? (y/n)")
               if roll_chance.lower() != 'y' :
                    break
          
               score_roll = roll()
               if score_roll == 1 :
                    print("ah you rolled 1 , your tern is done")
                    current_score = 0    
                    break
               else :
                    current_score += score_roll  
                    print(f'you got {score_roll} point')
               
               players_score[players_index] += current_score      
               print(f'your total score is {current_score} point')
    
         
          print(f'your total score is : {players_score[players_index]} for player {players_index + 1}')