import sys
import os
import csv
import subprocess as sub
from tabnanny import check
import time
names = []
with open('repoName.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        names.append(row[0])
# with open("correct.txt","r") as f:
#     correct = f.read()
correct = b"CSCI3081W Lab 2 - Classes\n=========================\nDisplay using vector\n=========================\nName: Unknown\nType: Unknown\nColor: Unknown\n-------------------------\nName: King\nType: Canvasback\nColor: brown-white\n-------------------------\nName: Mob\nType: Mallard\nColor: green-white\n-------------------------\n\n=========================\nDisplay using object class\n=========================\nName: Unknown\nType: Unknown\nColor: Unknown\nMother: Unknown\n-------------------------\nName: King\nType: Canvasback\nColor: brown-white\nMother: Unknown\n-------------------------\nName: Mob\nType: Mallard\nColor: green-white\nMother's Name: Whity\nMother's Type: Mallard\nMother's Color: green-white\n-------------------------\nName: White\nType: Mallard\nColor: green-white\nMother's Name: Whity\nMother's Type: Mallard\nMother's Color: green-white\n-------------------------\n"
print(names)
path  = os.getcwd()+"/student"
print(path)
makeerror=[]
fullmark = []
for name in names:
    clone = "git clone git@github.umn.edu:umn-csci-3081-F22/"+name+"-lab02.git" 

    os.chdir(path) # Specifying the path where the cloned project needs to be copied
    os.system(clone) # Cloning
    try:
        sub.check_call(["make"], cwd=os.getcwd()+"/"+name+"-lab02")
    except:
        makeerror.append(name)
    
for name in names:
    time.sleep(2)
    try:
        print("trying")
        out = sub.check_output(["./run"],cwd=os.getcwd()+"/"+name+"-lab02")
        if out==correct:
            fullmark.append(name)
        print(out)

    except:
        pass
print(fullmark)
    