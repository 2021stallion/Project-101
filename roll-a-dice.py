import random

no = "y"

while (no == "y"):
    no = random.randint(1,6)
    if (no==1):
        print("[-----]")
        print("[     ]")
        print("[  O  ]")
        print("[     ]")
        print("[-----]")
        no = input("Enter y to continue and n to exit.")
    elif (no==2):
        print("[-----]")
        print("[ O   ]")
        print("[     ]")
        print("[    O]")
        print("[-----]")
        no = input("Enter y to continue and n to exit.")
    elif (no==3):
        print("[-----]")
        print("[O    ]")
        print("[  O  ]")
        print("[    O]")
        print("[-----]")
        no = input("Enter y to continue and n to exit.")
    elif (no==4):
        print("[-----]")
        print("[O   O]")
        print("[     ]")
        print("[O   O]")
        print("[-----]")
        no = input("Enter y to continue and n to exit.")
    elif (no==5):
        print("[-----]")
        print("[O   O]")
        print("[  O  ]")
        print("[O   O]")
        print("[-----]")
        no = input("Enter y to continue and n to exit.")
    elif (no==6):
        print("[-----]")
        print("[ O O ]")
        print("[ O O ]")
        print("[ O O ]")
        print("[-----]")
        no = input("Enter y to continue and n to exit.")
