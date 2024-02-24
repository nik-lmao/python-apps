import requests
import colorama
colorama.init()

#Functions

def checkToken(token):
    r = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
    return r.status_code

invalid = []

def printResult(status, token):
    if status == 200: color = colorama.Fore.GREEN
    elif status == 429: color = colorama.Fore.YELLOW
    else: 
        color = colorama.Fore.RED
        invalid.append(token) 
    print(color + str(status) + colorama.Fore.LIGHTBLACK_EX + f" | {token}")
    
#Main

def main():
    print(colorama.Fore.LIGHTBLACK_EX + "Checking tokens...")
    tokens = open("tokens.txt", "r").read().splitlines()
    for token in tokens:
        printResult(checkToken(token), token)
    for token in invalid:
        tokens.remove(token)
    print(colorama.Fore.LIGHTBLACK_EX + "Removing invalid tokens...")
    with open("tokens.txt", "w") as f:
        for token in tokens:
            f.write(token + "\n")
    print(colorama.Fore.RESET + "Done!")
    while True:
        pass

main()