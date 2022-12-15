import os

print("What directory should the files be saved to? (Default directory is documents")
dir = input()

if(len(dir) == 0):
    if os.name == "nt":
        dir = "C:\\Documents\\"
    else:
        dir = "/home/Documents/"

# Temp solution, does not use dir
try:
    os.mkdir("ValorantAI")
    attack_path = os.path.join("ValorantAI", "Attack")
    defense_path = os.path.join("ValorantAI", "Defense")
    os.mkdir(attack_path)
    os.mkdir(defense_path)
except FileExistsError:
    pass # Just use existing dirs

