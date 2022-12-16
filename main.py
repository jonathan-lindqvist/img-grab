import os
from selenium import webdriver
import shutil
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
    access = 0o777
    os.mkdir("ValorantAI", mode=access)
    os.mkdir(attack_path, mode=access)
    os.mkdir(defense_path, mode=access)
except FileExistsError:
    pass # Just use existing dirs

# Next feature
# open browser [DONE]
# Screenshot [DONE]
# Save to dir [DONE]
# Open demo 
# play demo
# screenshot rounds
# Screenshot Crop image
# save into corresponding folder
# loop
driver = webdriver.Firefox()
driver.get("https://google.com")

driver.save_screenshot("test.png")
shutil.move("test.png", os.path.join(attack_path,"test.png"))
print("screenshot taken")