import os
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

print("What directory should the files be saved to? (Default directory is documents")
dir = input()

if(len(dir) == 0):
    if os.name == "nt":
        dir = "C:\\Documents\\"
    else:
        dir = "/home/Documents/"


attack_path = os.path.join("ValorantAI", "Attack")
defense_path = os.path.join("ValorantAI", "Defense")
# Temp solution, does not use dir
try:
    os.mkdir("ValorantAI")
    os.mkdir(attack_path)
    os.mkdir(defense_path)
except FileExistsError:
    pass # Just use existing dirs

# Next feature
# open browser
# Screenshot
# Screenshot specific area
# Save to dir
# Open demo 
# play demo
# screenshot rounds
# save into corresponding folder
browser = Firefox()
browser.get("https://google.com")


