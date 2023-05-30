from generator import *
from MinHeap import *
from game import *

with open("data_players.json", "w") as file_colas:
    json.dump([], file_colas, indent=4)

save_as_json("data_players.json", 8)

with open("data_players.json", "r+") as file:
    data = json.load(file)

minheap = MinHeap(len(data))

for i in range (0, len(data)):
    minheap.insert(data[i]['experience'])

for j in range(0, len(data)//2):
    experience1 = minheap.removeMin()
    experience2 = minheap.removeMin()
    for k in range(0, len(data)):
        if(data[k]["experience"] == experience1):
            name1 = data[k]["name"]
        if(data[k]["experience"] == experience2):
            name2 = data[k]["name"]
    player1, player2, msj = game()
    print(f'{name1} : {experience1} -> ({player1}) Vs. {name2} : {experience2} -> ({player2}) - Win: {msj}')


