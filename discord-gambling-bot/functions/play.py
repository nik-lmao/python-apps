import json
from random import randint

def update(id, amount):
    with open("./money.json", "r") as f:
        data = json.load(f)
    
    data[str(id)] = amount

    with open("./money.json", "w") as f:
        json.dump(data, f)




def play(id, bet):
    with open("./money.json", "r") as f:
        data = json.load(f)
    

    if str(id) not in data:
        data[str(id)] = 20
        with open("./money.json", "w") as f:
            json.dump(data, f)

    money = data[str(id)]



    if money == 0:
        return "You have lost the game! You have no money left!"
    elif bet < 0:
        return "You can't bet a negative amount of money!"
    elif bet == 0:
        return "You can't bet nothing!"
    elif bet > money:
        return "You can't bet more money than you have!"
    else:
        chance = randint(1,100)


        if chance > 50:
            money += bet
            update(id, money)  
            status = "won"   
        else:
            money -= bet
            update(id, money)
            status = "lost"
        if money == 0:
            return f"You now have no money anymore! Loser!"
        return f"You {status}! You now have {money} coins!"