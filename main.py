import time, sys

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()


lest = []

import random, time, threading
try:
    import os
    os.system("title " + "Roblox Unclaimed Group Sniper,   Made By Federal#6666,    Github: github.com/FederalCodes")
except:
    pass
colorama.init(autoreset=True)
def sniper():
    global lest
    try:
        while True:
            if wannarange == "n":
                groupid = random.randint(1, 15000000)
            if wannarange == "y":
                groupid = random.randint(rangeA, rangeB)
            groupid = str(groupid)
            id = str(groupid)
            r = requests.get("https://www.roblox.com/groups/group.aspx?gid="+str(groupid)).text
            r = str(r)
            if "owned" not in r:
                r2 = requests.get(f"https://groups.roblox.com/v1/groups/"+groupid)
                if "isLocked" not in r2.text and "owner" in r2.text:
                    entry = r2.json()["publicEntryAllowed"]
                    owner = r2.json()["owner"]
                    if entry == True and owner == None:
                        lest.append("Valid Group! https://roblox.com/groups/"+id)
                        if save == "y":
                            validfile = open("valid_groups.txt", "a")
                            validfile.write("https://roblox.com/groups/"+id+"\n")
                            validfile.close()
                        try:
                            r = requests.post(webhook, json={"content": "@here **Sniper Group** https://roblox.com/groups/"+id})
                        except:
                            pass
                else:
                    lest.append("Invalid Group! https://roblox.com/groups/"+id)
                    if save == "y":
                        invalidfile = open("invalid_groups.txt", "a")
                        invalidfile.write("https://roblox.com/groups/"+id+"\n")
                        invalidfile.close()
            else:
                lest.append("Invalid Group! https://roblox.com/groups/"+id)
                if save == "y":
                    invalidfile = open("invalid_groups.txt", "a")
                    invalidfile.write("https://roblox.com/groups/"+id+"\n")
                    invalidfile.close()
            time.sleep(float(delay))
    except:
        pass






def valid():
    sys.stdout.write(colorama.Fore.RED + "> ")
    print015("Enter A Valid Choice")



while True:
    try:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter How Many Threads (If To Many Printing The Codes Will Get Laggy): ")
        threads = input("")
        threads = int(threads)
        break
    except:
        valid()
while True:
    try:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Delay For Each Thread (0 = None): ")
        delay = input("")
        delay = float(delay)
        break
    except:
        print("Enter A Valid Chioce")


sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Enter Webhook To Send Unclaimed Groups Too (Leave Blank For None): ")
webhook = input("")
while True:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Wanna Auto Save All Groups (y/n): ")
    save = input("")
    if save == "y" or save == "n":
        break
    else:
        valid()


while True:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Wanna Pick Range (y/n, Advanced Option): ")
    wannarange = input("")
    if wannarange == "y" or wannarange == "n":
        break
    else:
        valid()


if wannarange == "y":
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("What Shall The Minimum Range Be: ")
            rangeA = input("")
            rangeA = int(rangeA)
            break
        except:
            valid()
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("What Shall The Maximum Range Be: ")
            rangeB = input("")
            rangeB = int(rangeB)
            break
        except:
            valid()



for u in range(int(threads)):
    t1 = threading.Thread(target=sniper)
    t1.start()
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print("Started Thread")
den = 0

while True:
    for u in lest:
        lest.remove(u)
        den = int(den) + 1
        if "Valid" in u:
            print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Unclaimed Group Found, https://roblox.com/groups/{colorama.Fore.CYAN}{str(u[39:])}")
        if "Invalid" in u:
            print(f"{colorama.Fore.RED}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.RED}]{colorama.Fore.RESET} Claimed Group Found, https://roblox.com/groups/{colorama.Fore.RED}{str(u[41:])}")
