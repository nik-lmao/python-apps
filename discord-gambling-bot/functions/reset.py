import json

def reset(id):
    with open("./money.json", "r") as f:
        data = json.load(f)
    
    data[str(id)] = 20

    with open("./money.json", "w") as f:
        json.dump(data, f)

    return "Your balance has been reset to 20 coins!"