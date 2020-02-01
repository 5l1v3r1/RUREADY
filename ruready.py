import random
import pyfiglet
import time
import os

u = input("Do you want to play a game ? Yes/No ?\n")

if u == 'Yes':
    print(" ")
    ascii_banner = pyfiglet.figlet_format("ROCK PAPER SCISSORS")
    print(ascii_banner)
    group = ["Rock","Paper","Scissors","Boris Johnson"]
    action = {"Rock": "\nRock beats Scissors.", "Paper": "\nPaper beats Rock.", "Scissors": "\nScissors beats Paper.",
          "Boris Johnson": "\nBoris Johnson show us his dick, the game is over."}
    cpu = group[random.randint(0,3)]
    print("LOADING...")
    time.sleep(3.0)
    print("Choose your weapon !!! Rock,Paper or Scissors ?")
    user = input()
    print("You choose " + user + ". ")
    time.sleep(2.0)
    print("\nComputer choose " + cpu + ".")

    time.sleep(2.0)

    if (cpu == user):
        print("wtf")
    else:
        if group.index(user) - group.index(cpu) in range(0,3):
            print(action[user])
            print("GG")
        else:
            print(action[cpu])
            print("You're a piece of shit")

    time.sleep(2.0)
        
    print("OK...")

    time.sleep(4.0)

    ascii_banner = pyfiglet.figlet_format("R U READY ?")
    print(ascii_banner)
    print("RUREADY V1.1 - A TOOL BY UAYEB5")
    print("WARNING ! THIS TOOL IS FOR EDUCATIONAL PURPOSE ONLY !\n")
    print(" ")

    time.sleep(2.0)

    a = input("Do you want to continue ? Yes/No ?\n")
    b = input("What do you want to do ?\nFind a victim for SQL Injection 1 ? for XSS Cross Site Scripting 2 ?\n")

    if a == 'Yes':
        print(" ")
              
    elif a == 'No':
        print(" ")
        print("Sorry, Bye.")
        raise SystemExit

    else:
        print(" ")
        print("Are you high ? Bye.")
        raise SystemExit

    if b == '1':
        print(" ")
        os.system('python3 sql.py')
    
    elif b == '2':
        print(" ")
        os.system('python3 xss.py')
    
    else:
        print(" ")
        print("Are you high ? Bye.")
        raise SystemExit
              
elif u == 'No':
    print(" ")
    ascii_banner = pyfiglet.figlet_format("R U READY ?")
    print(ascii_banner)
    print("RUREADY V1.1 - A TOOL BY UAYEB5")
    print("WARNING ! THIS TOOL IS FOR EDUCATIONAL PURPOSE ONLY !\n")

    time.sleep(2.0)

    a = input("Do you want to continue ? Yes/No ?\n")
    b = input("What do you want to do ?\nFind a victim for SQL Injection 1 ? for XSS Cross Site Scripting 2 ?\n")

    if a == 'Yes':
        print(" ")
                    
    elif a == 'No':
        print(" ")
        print("Sorry, Bye.")
        raise SystemExit

    else:
        print(" ")
        print("Are you high ? Bye.")
        raise SystemExit

    if b == '1':
        print(" ")
        os.system('python3 sql.py')
    
    elif b == '2':
        print(" ")
        os.system('python3 xss.py')
    
    else:
        print(" ")
        print("Are you high ? Bye.")
        raise SystemExit

else:
        print(" ")
        print("Are you high ? Bye.")
        raise SystemExit