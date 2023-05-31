from generator import *
from MinHeap import *
from game import *

with open("data_players.json", "w") as file_colas:
    json.dump([], file_colas, indent=4)

save_as_json("data_players.json", 32)

with open("data_players.json", "r+") as file:
    data = json.load(file)

minheap = MinHeap(len(data))


def match(number):
    print("---------------" * 3)
    print(f'{number} ROUND')
    print("---------------" * 3)
    for i in range(0, len(data)):
        minheap.insert(data[i]['experience'])
    try:
        while len(data) > 1:
            experience1 = minheap.removeMin()
            experience2 = minheap.removeMin()

            for k in range(0, len(data)):

                if (data[k]["experience"] == experience1):
                    name1 = data[k]["name"]
                    number1 = k

                if (data[k]["experience"] == experience2):
                    name2 = data[k]["name"]
                    number2 = k

            player1, player2, msj = game()
            print(
                f'{name1} |EXP:{experience1}| |({player1})|  Vs.  {name2} |EXP:{experience2}| |({player2})| -- Winner: {msj}\n')

            if (msj == "Player 1"):
                data.pop(number2)
            else:
                data.pop(number1)
    except:
        match(number + 1)


match(1)
print(
    f'The champion is: {data[0]["name"]} with experience: {data[0]["experience"]}')
