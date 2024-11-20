import random as ra

starters = ["b", "r", "h", "t", "c", "x", "q"]
centers = ["a", "o", "e", "u", "y"]
breakers = ["m", "n", "p", "d", "c", "k", "l"]
enders = ["z", "x", "p", "o", "q", "r", "d", "h"]

names = []

def generate_name():
    return (starters[ra.randint(0, len(starters) - 1)] +
            centers[ra.randint(0, len(centers) - 1)] +
            breakers[ra.randint(0, len(breakers) - 1)] +
            centers[ra.randint(0, len(centers) - 1)] +
            enders[ra.randint(0, len(enders) - 1)])
print("  _    _  _____ ______ _____  _   _          __  __ ______      \n | |  | |/ ____|  ____|  __ \\| \\ | |   /\\   |  \\/  |  ____|     \n | |  | | (___ | |__  | |__) |  \\| |  /  \\  | \\  / | |__        \n | |  | |\\___ \\|  __| |  _  /| . ` | / /\\ \\ | |\\/| |  __|       \n | |__| |____) | |____| | \\ \\| |\\  |/ ____ \\| |  | | |____      \n  \\____/|_____/|______|_|__\\_\\_|_\\_/_/    \\_\\_|__|_|______|___  \n  / ____|  ____| \\ | |  ____|  __ \\     /\\|__   __/ __ \\|  __ \\ \n | |  __| |__  |  \\| | |__  | |__) |   /  \\  | | | |  | | |__) |\n | | |_ |  __| | . ` |  __| |  _  /   / /\\ \\ | | | |  | |  _  / \n | |__| | |____| |\\  | |____| | \\ \\  / ____ \\| | | |__| | | \\ \\ \n  \\_____|______|_| \\_|______|_|  \\_\\/_/    \\_\\_|  \\____/|_|  \\_\\\n                                                                \n                                                                \n")
print("Welcome to Cybers Username Generator. Generate 5 letter usernames that actually WORK and are not nvchysdgbf or starryeyedfish17 \n")

howmany = input("How many names to generate?: ")

for i in range(int(howmany)):
    name = generate_name()
    print(name)
    names.append(name)

save = input("Save to text file? y/n ")

if save == "y":
    textfile = open("names.txt", "w")
    for i in names:
        textfile.write(i + ", \n")
    print("Text file made")
    textfile.close()
    input("Thanks for using cybers username generator (Enter to close)")
else:
    input("Thanks for using cybers username generator (Enter to close)")
