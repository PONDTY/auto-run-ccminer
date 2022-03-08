import os, json, requests

def versionApp():
    with open("version.json", encoding="utf-8") as read:
        load = read.read()
        loads = json.loads(load)
        return loads['version']

# banner function
def banner():


    os.system("@cls||clear")
    print(f"Created by.mobile-mining V{versionApp()}")
    print("---------------------------------------------------") 
    print("\033[96mpp miner\033[00m\n")
    print("---------------------------------------------------")
