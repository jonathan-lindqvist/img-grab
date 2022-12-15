import os

print("What directory should the files be saved to? (Default directory is documents")
dir = input()

if(len(dir) == 0):
    if os.name == "nt":
        dir = "C:\\Documents\\"
    else:
        dir = "/home/Documents/"

try:
    os.makedirs(dir + "ValorantAI")
    os.makedirs(dir + "ValorantAI/Attack")
    os.makedirs(dir + "ValorantAI/Defense")
except FileExistsError:
    pass # Just use existing dirs

