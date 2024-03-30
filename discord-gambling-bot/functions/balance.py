import json

def balance(id):
    with open("./money.json", "r") as f:
        data = json.load(f)
    
    money = data[str(id)]
    return f"You have {money} coins!"