import json
import os

# way to project main file
BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/ninja_fruits"


#counter_strike = 0

#while counter_strike < 3:
 #   counter_strike = counter_strike+1
 #   print("b")
 #boucle de jeu

# empty list 
player= []

def add_points(score_container, player_name, points):
    for element in score_container:
        if element["name"] == player_name:
            element["score"] += points
            return score_container

# Il faudra changer les entrées ici
player_name =input("Nom :")
points= int(input("score :"))
    # read score.json
try:
    with open (os.path.join(BASE_DIR,"score.json"), "r") as f:
        score_container = json.load(f)  
# manage error cases
except FileNotFoundError:
    score_container = []
except json.JSONDecodeError:
    score_container= []        

# new score entry
add_points(score_container,player_name, points)
score_container.append({"name": player_name, "score": points})
    
# score in order
score_container = sorted(score_container, key=lambda player: player["score"], reverse=True)

# record in scor.json
with open (os.path.join(BASE_DIR,"score.json"), "w") as f:
        score_container= json.dump(score_container, f)

# Display Part

with open (os.path.join(BASE_DIR,"score.json"), "r") as f:
        player_list= json.load(f)      
for i, player in enumerate(player_list):
    print(f'{i+1}. {player["name"]} => {player["score"]}')